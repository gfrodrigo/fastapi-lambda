import json
import os
from ddtrace import tracer
from typing import Literal, Optional
from uuid import uuid4
from pydantic import BaseModel

BOOKS_FILE = "books.json"
BOOKS = []

if os.path.exists(BOOKS_FILE):
    with open(BOOKS_FILE, "r") as f:
        BOOKS = json.load(f)


class Book(BaseModel):
    name: str
    genre: Literal["fiction", "non-fiction"]
    price: float
    book_id: Optional[str] = uuid4().hex

    @staticmethod
    @tracer.wrap(service="fastapi", resource="model/list-books", span_type="sql")
    def list_items():
        return BOOKS
