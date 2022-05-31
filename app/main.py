"""FastAPI Entrypoint"""
from fastapi import FastAPI

from app import logger
from app.api.controllers import starlink_tracker, starlink_load_data


app = FastAPI()

app.include_router(starlink_tracker.router, prefix="", tags=["starlink_tracker"])
app.include_router(starlink_load_data.router, prefix="", tags=["starlink_load_data"])
