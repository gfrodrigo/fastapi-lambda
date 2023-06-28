from ddtrace import tracer
from fastapi import FastAPI
from mangum import Mangum

import models
from database import engine
from routers import api

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api.api_router, prefix="/api", tags=["api"])
app.include_router(api.api_router, prefix="/services", tags=["services"])
handler = Mangum(app)


@app.get("/")
@tracer.wrap(service="fastapi", resource="GET /", span_type="web")
async def root():
    return {"message": "Hello Bigger Applications!"}
