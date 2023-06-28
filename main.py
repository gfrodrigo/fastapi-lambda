from ddtrace import tracer
from fastapi import FastAPI
from mangum import Mangum

import models
from database import engine
from routers import books

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(books.router, prefix="/books2", tags=["books2"])
app.include_router(books.router, prefix="/books3", tags=["books3"])
app.include_router(books.router, prefix="/books4", tags=["books4"])
app.include_router(books.router, prefix="/books5", tags=["books5"])
app.include_router(books.router, prefix="/books6", tags=["books6"])
app.include_router(books.router, prefix="/books7", tags=["books7"])
app.include_router(books.router, prefix="/books8", tags=["books8"])
app.include_router(books.router, prefix="/books9", tags=["books9"])
handler = Mangum(app)


@app.get("/")
@tracer.wrap(service="fastapi", resource="GET /", span_type="web")
async def root():
    return {"message": "Hello Bigger Applications!"}
