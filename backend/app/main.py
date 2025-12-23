from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from app.routes.movie_routes import router as movie_router


app = FastAPI(title="Movie Ticket Booking API")


app.include_router(auth_router)
app.include_router(movie_router)


@app.get("/")
def health():
    return {"status": "Backend running"}