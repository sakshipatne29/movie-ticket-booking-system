from datetime import datetime

def booking_document(show_id, seats, email):
    return {
        "show_id": show_id,
        "seats": seats,
        "email": email,
        "payment_status": "PENDING",
        "booking_status": "LOCKED",

        "locked_at": datetime.now(),  # USED for auto-release
        "created_at": datetime.now()
    }
