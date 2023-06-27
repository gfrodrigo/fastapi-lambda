from model import Book
from ddtrace import tracer


class BookService:
    def __init__(self):
        self.model = Book

    @tracer.wrap(service="fastapi", resource="service/list-books", span_type="service")
    def list(self):
        return self.model.list_items()
