import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .csv_service import FILES, read_all, read_csv

app = FastAPI(
    title="AMR Lab Content API",
    description="CSV-driven content API for the AMR Lab website at IIT Ropar.",
    version="1.0.0",
)

# Add the production GitHub Pages origin and local development origins.
allowed_origins = [
    "https://navjotsig.github.io",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]
extra_origins = os.getenv("CORS_ORIGINS", "")
allowed_origins.extend([x.strip() for x in extra_origins.split(",") if x.strip()])

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok", "service": "AMR Lab Content API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/content")
def all_content():
    return read_all()

@app.get("/api/{section}")
def section_content(section: str):
    if section not in FILES:
        raise HTTPException(status_code=404, detail="Unknown content section")
    return {"items": read_csv(section)}
