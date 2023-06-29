import json
import os

from ddtrace import tracer
from sqlalchemy import Column, Integer, String, Float

from src.database import Base

BOOKS_FILE = "../../books.json"
BOOKS = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOKS = json.load(f)


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    genre = Column(String)
    price = Column(Float)

    @staticmethod
    @tracer.wrap(service="fastapi", resource="model/list-books", span_type="sql")
    def list_items():
        return BOOKS
