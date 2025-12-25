from fastapi import APIRouter
from app.database import db

router = APIRouter(prefix="/theatres", tags=["Theatres"])

@router.post("/")
def add_theatre(theatre: dict):
    db.theatres.insert_one(theatre)
    return {"message": "Theatre added"}

@router.get("/")
def list_theatres():
    return list(db.theatres.find({}, {"_id": 0}))
