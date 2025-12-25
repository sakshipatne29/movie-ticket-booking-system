from fastapi import APIRouter, HTTPException
from datetime import datetime
from bson import ObjectId
from app.utils.auto_release import release_expired_locks

from app.database import db
from app.schemas.booking_schema import SeatLockRequest, PaymentRequest
from app.models.booking_model import booking_document

router = APIRouter(prefix="/bookings", tags=["Bookings"])

LOCK_EXPIRY_MINUTES = 10
@router.post("/lock")
def lock_seats(payload: SeatLockRequest):
    release_expired_locks()
    show_id = ObjectId(payload.show_id)

    show = db.shows.find_one({"_id": show_id})
    if not show:
        raise HTTPException(status_code=404, detail="Show not found")

    # ❗ Check for seat conflicts
    conflict = db.bookings.find_one({
        "show_id": show_id,
        "seats": {"$in": payload.seats},
        "booking_status": {"$in": ["LOCKED", "CONFIRMED"]}
    })

    if conflict:
        raise HTTPException(status_code=400, detail="Seat already booked")

    booking = booking_document(
        show_id=show_id,
        seats=payload.seats,
        email=payload.email
    )

    result = db.bookings.insert_one(booking)

    return {
        "message": "Seats locked successfully",
        "booking_id": str(result.inserted_id),
        "expires_in_minutes": LOCK_EXPIRY_MINUTES
    }

@router.post("/pay")
def simulate_payment(payload: PaymentRequest):
    booking_id = ObjectId(payload.booking_id)

    booking = db.bookings.find_one({
        "_id": booking_id,
        "email": payload.email
    })

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking["booking_status"] != "LOCKED":
        raise HTTPException(status_code=400, detail="Booking not in payable state")

    # Mark booking as confirmed
    db.bookings.update_one(
        {"_id": booking_id},
        {
            "$set": {
                "payment_status": "SUCCESS",
                "booking_status": "CONFIRMED"
            }
        }
    )

    # Permanently book seats
    db.shows.update_one(
        {"_id": booking["show_id"]},
        {
            "$addToSet": {
                "booked_seats": {"$each": booking["seats"]}
            }
        }
    )

    return {"message": "Payment successful, booking confirmed"}