"""FastAPI Entrypoint"""
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from app import db_url
from app.api.controllers import starlink_tracker, starlink_load_data


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=db_url)

app.include_router(starlink_tracker.router, prefix="", tags=["starlink_tracker"])
