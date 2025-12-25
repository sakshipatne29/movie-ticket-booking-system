from fastapi import APIRouter
from app.database import db
from bson import ObjectId

router = APIRouter(prefix="/shows", tags=["Shows"])

@router.post("/")
def create_show(show: dict):
    show["booked_seats"] = []
    db.shows.insert_one(show)
    return {"message": "Show created"}

@router.get("/{show_id}/seats")
def get_seat_status(show_id: str):
    show = db.shows.find_one({"_id": ObjectId(show_id)})
    return {
        "booked_seats": show["booked_seats"]
    }
