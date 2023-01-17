import uvicorn

from fastapi import FastAPI
from api.api import api_router
from handlers import root_router
from fastapi.staticfiles import StaticFiles
from db.database import database, metadata, engine
from config import API_METADATA


app = FastAPI(
    title=API_METADATA.get("title"),
    version=API_METADATA.get("version"),
    description=API_METADATA.get("description"),
    terms_of_service=API_METADATA.get("terms_of_service"),
    contact=API_METADATA.get("contact"),
    license_info=API_METADATA.get("license_info"),
    openapi_url="/api/openapi.json"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

metadata.create_all(engine)
app.state.database = database


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

app.include_router(api_router)
app.include_router(root_router)

if __name__ == "__main__":
    uvicorn.run('main:app', port=80, host='127.0.0.1', reload=True)
