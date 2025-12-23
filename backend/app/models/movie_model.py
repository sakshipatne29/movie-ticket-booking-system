from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    title: str
    description: str
    duration: int   # minutes
    language: str
    genre: str
    rating: Optional[float] = None
