from ddtrace import tracer
from fastapi import FastAPI
from mangum import Mangum

import models
from database import engine
from routers import books

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(books.router)
handler = Mangum(app)


@app.get("/")
@tracer.wrap(service="fastapi", resource="GET /", span_type="web")
async def root():
    return {"message": "Hello Bigger Applications!"}
