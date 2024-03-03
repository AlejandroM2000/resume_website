"""Flask APP configuration."""
from os import environ, path
from dotenv import load_dotenv


# Specificy a `.env` file containing key/value config values
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
    # General Config
    DB_USER = environ.get("DB_USER")
    DB_NAME = environ.get("DB_NAME")
    DB_HOST = environ.get("DB_HOST")
    DB_PASSWORD = environ.get("DB_PASSWORD")
    DB_PORT = environ.get("DB_PORT")
    DB_URL = environ.get("DB_URL")

    # Database
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False