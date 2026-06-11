from fastapi import FastAPI

from app.database import Base, engine
import app.models.users

app = FastAPI(title="DeskDibs API", version="1.0.0")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/api/health")
def health():
    return {"status": "ok"}