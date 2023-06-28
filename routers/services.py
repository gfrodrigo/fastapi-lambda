from routers import books
from fastapi import APIRouter

services_router = APIRouter()
services_router.include_router(books.router, prefix="/books", tags=["books"])
services_router.include_router(books.router, prefix="/books2", tags=["books2"])
services_router.include_router(books.router, prefix="/books3", tags=["books3"])
services_router.include_router(books.router, prefix="/books4", tags=["books4"])
services_router.include_router(books.router, prefix="/books5", tags=["books5"])
services_router.include_router(books.router, prefix="/books6", tags=["books6"])
services_router.include_router(books.router, prefix="/books7", tags=["books7"])
services_router.include_router(books.router, prefix="/books8", tags=["books8"])
services_router.include_router(books.router, prefix="/books9", tags=["books9"])
