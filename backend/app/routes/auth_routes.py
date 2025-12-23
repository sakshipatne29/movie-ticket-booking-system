from fastapi import APIRouter, HTTPException
from app.database import db
from app.utils.password_hash import hash_password, verify_password
from app.utils.jwt_handler import create_access_token


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
def register(email: str, password: str):
    if db.users.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="User already exists")
        db.users.insert_one({
        "email": email,
        "password": hash_password(password),
        "role": "user"
        })
        return {"message": "User registered"}


@router.post("/login")
def login(email: str, password: str):
    user = db.users.find_one({"email": email})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
        token = create_access_token({"sub": email, "role": user["role"]})
        return {"access_token": token}