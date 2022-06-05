"""Starlink Historical Data model module"""
from sqlalchemy import Column, Integer, String, Float, DateTime
from app import Base


class StarlinkHistoricalData(Base):
    """Starlink Historical Data Database Model

    Args:
        Base (SQLAlchemy): MySql entity
    """
    __tablename__ = 'startlink_historical_data'

    row_id = Column(Integer, primary_key=True)
    satellite_id = Column("id", String)
    creation_date = Column("spacetrack_creation_date", DateTime)
    latitude = Column("latitude", Float)
    longitude = Column("longitude", Float)
