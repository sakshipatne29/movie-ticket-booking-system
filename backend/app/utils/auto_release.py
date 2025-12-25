from datetime import datetime, timedelta
from app.database import db

LOCK_EXPIRY_MINUTES = 10

def release_expired_locks():
    expiry_time = datetime.now() - timedelta(minutes=LOCK_EXPIRY_MINUTES)

    expired_bookings = db.bookings.find({
        "booking_status": "LOCKED",
        "locked_at": {"$lt": expiry_time}
    })

    for booking in expired_bookings:
        db.bookings.update_one(
            {"_id": booking["_id"]},
            {"$set": {"booking_status": "EXPIRED"}}
        )
