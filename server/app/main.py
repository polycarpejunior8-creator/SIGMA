"""
SIGMA SERVER — point d'entrée de l'API.

Démarrage :
    uvicorn app.main:app --host 0.0.0.0 --port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api.routers import (
    auth, organizations, users, posts, delegations, audit,
    academic_structure, students, assessments, finance, dashboard,
    attendance, honor_boards, timetable, hr, communication, report_cards,
)

app = FastAPI(
    title="SIGMA — Système Intégré de Gestion et Management Académique",
    description="API centrale du serveur SIGMA (cf cahier des charges v2.0).",
    version="0.1.0-mvp",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(organizations.router)
app.include_router(users.router)
app.include_router(posts.router)
app.include_router(delegations.router)
app.include_router(audit.router)
app.include_router(academic_structure.router)
app.include_router(students.router)
app.include_router(assessments.router)
app.include_router(finance.router)
app.include_router(dashboard.router)
app.include_router(attendance.router)
app.include_router(honor_boards.router)
app.include_router(timetable.router)
app.include_router(hr.router)
app.include_router(communication.router)
app.include_router(report_cards.router)


@app.get("/api/health", tags=["Santé"])
def health_check():
    return {"status": "ok", "service": "SIGMA Server"}
