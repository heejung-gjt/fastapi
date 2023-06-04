from typing import Final, Optional
import os
from dotenv import dotenv_values

def getenv(key: str) -> str:
    return dotenv_values(".env")


STAGE: Final[str] = getenv("ENVIRONMENT")

# DB
DB_HOST: Final[str] = getenv("DB_HOST")
DB_PORT: Final[str] = getenv("DB_PORT")
DB_DATABASE: Final[str] = getenv("DB_DATABASE")
DB_USER: Final[str] = getenv("DB_USER")
DB_PASSWORD: Final[str] = getenv("DB_PASSWORD")


DATABASES = {
    "default": "helper",
    "DATABASE": {
        "helper": {
            "ENGINE": "django.db.backends.postgresql",
            "DB_HOST": DB_HOST,
            "DB_PORT": DB_PORT,
            "DB_NAME": DB_DATABASE,
            "DB_USER": DB_USER,
            "DB_PASSWORD": DB_PASSWORD,
            "MIN_SIZE": 10,
            "MAX_SIZE": 50
        },
    }
}