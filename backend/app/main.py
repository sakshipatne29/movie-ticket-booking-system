from fastapi import FastAPI
from app.routes.auth_routes import router as auth_router
from app.routes.movie_routes import router as movie_router
from app.routes import movie_routes, theatre_routes, show_routes, booking_routes


app = FastAPI(title="Movie Ticket Booking API")


app.include_router(auth_router)
app.include_router(movie_router)

app.include_router(movie_routes.router)
app.include_router(theatre_routes.router)
app.include_router(show_routes.router)
app.include_router(booking_routes.router)

@app.get("/")
def health():
    return {"status": "Backend running"}