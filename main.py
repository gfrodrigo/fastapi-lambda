import random

from ddtrace import tracer
from fastapi import FastAPI, HTTPException
from mangum import Mangum

import models
from database import engine
from service import BookService

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
handler = Mangum(app)


@app.get("/")
@tracer.wrap(service="fastapi", resource="GET /", span_type="web")
async def root():
    return {"message": "Welcome to my bookstore app!"}


@app.get("/random-book")
@tracer.wrap(service="fastapi", resource="GET /list-books", span_type="web")
async def random_book():
    return random.choice(BookService().list())


@app.get("/list-books")
@tracer.wrap(service="fastapi", resource="GET /list-books", span_type="web")
async def list_books():

    return {"books": BookService().list()}


@app.get("/book_by_index/{index}")
async def book_by_index(index: int):
    books = BookService().list()
    if index < len(books):
        return books[index]
    else:
        raise HTTPException(404, f"Book index {index} out of range ({len(books)}).")


# @app.post("/add-book")
# async def add_book(book: Book):
#     book.book_id = uuid4().hex
#     json_book = jsonable_encoder(book)
#     books = BookService().list()
#     books.append(json_book)
#
#     with open(BOOKS_FILE, "w") as f:
#         json.dump(books, f)
#
#     return {"book_id": book.book_id}


@app.get("/get-book")
async def get_book(book_id: str):
    for book in BookService().list():
        if book.book_id == book_id:
            return book

    raise HTTPException(404, f"Book ID {book_id} not found in database.")
