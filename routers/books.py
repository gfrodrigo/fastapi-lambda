import random
from service import BookService
from fastapi import APIRouter, HTTPException
from ddtrace import tracer

router = APIRouter()


@router.get("/random-book")
@tracer.wrap(service="fastapi", resource="GET /list-books", span_type="web")
async def random_book():
    return random.choice(BookService().list())


@router.get("/list-books")
@tracer.wrap(service="fastapi", resource="GET /list-books", span_type="web")
async def list_books():
    return {"books": BookService().list()}


@router.get("/book_by_index/{index}")
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


@router.get("/get-book")
async def get_book(book_id: str):
    for book in BookService().list():
        if book.book_id == book_id:
            return book

    raise HTTPException(404, f"Book ID {book_id} not found in database.")
