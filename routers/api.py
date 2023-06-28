from routers import books
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(books.router, prefix="/books", tags=["books"])
api_router.include_router(books.router, prefix="/books2", tags=["books2"])
api_router.include_router(books.router, prefix="/books3", tags=["books3"])
api_router.include_router(books.router, prefix="/books4", tags=["books4"])
api_router.include_router(books.router, prefix="/books5", tags=["books5"])
api_router.include_router(books.router, prefix="/books6", tags=["books6"])
api_router.include_router(books.router, prefix="/books7", tags=["books7"])
api_router.include_router(books.router, prefix="/books8", tags=["books8"])
api_router.include_router(books.router, prefix="/books9", tags=["books9"])
