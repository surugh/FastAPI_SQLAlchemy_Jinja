import uvicorn

from fastapi import FastAPI
from api.api import api_router
from handlers import root_router
from fastapi.staticfiles import StaticFiles
from db.database import database, metadata, engine

description = """
PG Tech DEV
"""

app = FastAPI(
    title="FastAPI & SQLAlchemy & Jinja",
    description=description,
    version="0.0.1",
    terms_of_service="https://opensource.org/licenses/MIT",
    contact={
        "name": "Paranoya Games",
        "url": "https://t.me/paranoya_games",
        "telegram": "https://t.me/get_gl",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
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
