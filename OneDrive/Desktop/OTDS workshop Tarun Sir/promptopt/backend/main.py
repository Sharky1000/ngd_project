from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import runs, export
from database import init_db

app = FastAPI(title="PromptOpt Backend", version="2.0")

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(runs.router)
app.include_router(export.router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Root endpoint
@app.get("/")
def root():
    return {
        "message": "PromptOpt API",
        "docs": "/docs",
        "health": "/health"
    }

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()
    print("✅ Database initialized")