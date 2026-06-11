from fastapi import FastAPI

from app.database import Base, engine
from app.routers import auth
import app.models.user  # noqa: F401

app = FastAPI(title="DeskDibs API", version="1.0.0")

app.include_router(auth.router, prefix="/api")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/api/health")
def health():
    return {"status": "ok"}