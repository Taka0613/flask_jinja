# config.py

import os


class Config:
    SECRET_KEY = "5d46460c43c79942c33111efaacb480e3b9367d1266320f047d3c2e7be17b8fe"  # Replace with a secure key in production
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
