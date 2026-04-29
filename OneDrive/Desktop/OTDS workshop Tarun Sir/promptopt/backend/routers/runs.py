from fastapi import APIRouter, HTTPException, BackgroundTasks
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
import json
import uuid
import sys
sys.path.append('..')
from database import get_db
from core.job_initializer import RunConfig

router = APIRouter(prefix="/runs", tags=["runs"])

@router.post("/")
async def create_run(config: RunConfig, background_tasks: BackgroundTasks):
    db = get_db()
    run_id = f"run-{uuid.uuid4().hex[:8]}"
    now = datetime.utcnow().isoformat()
    
    db.execute("""
        INSERT INTO runs (id, task_name, task_type, mode, base_prompt, scorer,
                         max_iterations, early_stop_threshold, variants_per_iter,
                         dataset_json, criteria_json, status, created_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (run_id, config.task_name, config.task_type, config.mode, config.base_prompt,
          config.scorer, config.max_iterations, config.early_stop_threshold,
          config.variants_per_iter, json.dumps(config.dataset or []),
          json.dumps(config.criteria or []), "queued", now))
    db.commit()
    
    # Start optimization in background
    # background_tasks.add_task(run_optimization, run_id)
    
    return {"id": run_id, "status": "queued", "created_at": now}

@router.get("/")
async def list_runs(status: Optional[str] = None, mode: Optional[str] = None, task_type: Optional[str] = None):
    db = get_db()
    query = "SELECT * FROM runs WHERE 1=1"
    params = []
    
    if status:
        query += " AND status = ?"
        params.append(status)
    if mode:
        query += " AND mode = ?"
        params.append(mode)
    if task_type:
        query += " AND task_type = ?"
        params.append(task_type)
    
    query += " ORDER BY created_at DESC"
    
    rows = db.execute(query, params).fetchall()
    return [dict(row) for row in rows]

@router.get("/{run_id}")
async def get_run(run_id: str):
    db = get_db()
    row = db.execute("SELECT * FROM runs WHERE id = ?", (run_id,)).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Run not found")
    return dict(row)

@router.delete("/{run_id}")
async def cancel_run(run_id: str):
    db = get_db()
    now = datetime.utcnow().isoformat()
    db.execute("""
        UPDATE runs SET status = 'failed', failure_reason = 'Cancelled by user', completed_at = ?
        WHERE id = ? AND status IN ('queued', 'running')
    """, (now, run_id))
    db.commit()
    return {"success": True}

@router.get("/{run_id}/variants")
async def get_variants(run_id: str):
    db = get_db()
    rows = db.execute(
        "SELECT * FROM prompt_variants WHERE run_id = ? ORDER BY iteration ASC",
        (run_id,)
    ).fetchall()
    return [dict(row) for row in rows]