from dotenv import load_dotenv
import os


load_dotenv()


class Settings:
    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME")
    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    JWT_EXPIRY_MINUTES = int(os.getenv("JWT_EXPIRY_MINUTES"))


settings = Settings()