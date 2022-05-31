"""Repository Sample module"""
from fastapi_sqlalchemy import db

from app.api.domain.models.satellite import StarlinkHistoricalData


def get_satellite_by_id(id: str):
    return db.session.query(StarlinkHistoricalData).filter(
        StarlinkHistoricalData.id == id
    ).first()
