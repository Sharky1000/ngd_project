from fastapi import APIRouter, HTTPException
from datetime import datetime
import sys
sys.path.append('..')
from database import get_db

router = APIRouter(prefix="/runs", tags=["export"])

@router.get("/{run_id}/export")
async def export_run(run_id: str, format: str = "text"):
    db = get_db()
    row = db.execute("SELECT * FROM runs WHERE id = ?", (run_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Run not found")
    
    if format == "json":
        return dict(row)
    else:
        return {"prompt": row["best_prompt"] or row["base_prompt"]}

@router.get("/{run_id}/versions")
async def get_versions(run_id: str):
    db = get_db()
    rows = db.execute(
        "SELECT * FROM prompt_variants WHERE run_id = ? ORDER BY score DESC",
        (run_id,)
    ).fetchall()
    
    return [
        {
            "id": row["id"],
            "version": i + 1,
            "label": f"Iteration {row['iteration']}",
            **dict(row)
        }
        for i, row in enumerate(rows)
    ]

@router.post("/registry")
async def save_to_registry(run_id: str):
    # Simplified - just mark as production
    db = get_db()
    db.execute(
        "UPDATE runs SET status = 'complete' WHERE id = ?",
        (run_id,)
    )
    db.commit()
    return {"success": True, "message": "Saved to registry"}

@router.get("/registry")
async def get_registry(status: str = None):
    db = get_db()
    query = "SELECT * FROM runs WHERE best_prompt IS NOT NULL"
    params = []
    
    if status:
        query += " AND status = ?"
        params.append(status)
    
    rows = db.execute(query, params).fetchall()
    return [dict(row) for row in rows]