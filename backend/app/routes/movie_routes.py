from fastapi import APIRouter
from app.database import db
from app.models.movie_model import Movie
from datetime import datetime

router = APIRouter(prefix="/movies", tags=["Movies"])

# @router.post("/")
# def add_movie(movie: Movie):
#     db.movies.insert_one(movie.dict())
#     return {"message": "Movie added successfully"}

# @router.get("/")
# def get_movies():
#     movies = list(db.movies.find({}, {"_id": 0}))
#     return movies
@router.post("/")
def add_movie(movie: Movie):
    movie["created_at"] = datetime.now()
    db.movies.insert_one(movie)
    return {"message": "Movie added successfully"}

@router.get("/")
def list_movies():
    return list(db.movies.find({}, {"_id": 0}))