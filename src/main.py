from ddtrace import tracer
from fastapi import FastAPI
from mangum import Mangum

from src.routers import api, services
from src.database import engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api.api_router, prefix="/api", tags=["api"])
app.include_router(services.services_router, prefix="/services", tags=["services"])
handler = Mangum(app)


@app.get("/")
@tracer.wrap(service="fastapi", resource="GET /", span_type="web")
async def root():
    return {"message": "Hello Bigger Applications!"}
