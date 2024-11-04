# config.py

import os


class Config:
    SECRET_KEY = "your_secret_key_here"  # Replace with a secure key in production
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
