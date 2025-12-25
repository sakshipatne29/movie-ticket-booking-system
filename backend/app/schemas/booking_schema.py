from pydantic import BaseModel, EmailStr
from typing import List

class SeatLockRequest(BaseModel):
    show_id: str
    email: EmailStr
    seats: List[str]

class PaymentRequest(BaseModel):
    booking_id: str
    email: EmailStr
    amount: float