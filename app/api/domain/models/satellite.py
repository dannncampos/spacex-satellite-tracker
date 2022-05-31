from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime

from app import Base


class StarlinkHistoricalData(Base):
    """Starlink Historical Data Database Model

    Args:
        Base (SQLAlchemy): MySql entity
    """
    __tablename__ = 'startlink_historical_data'

    row_id = Column(Integer, primary_key=True)
    id = Column("id", String)
    creation_date = Column("creation_date", DateTime)
    latitude = Column("latitude", String)
    longitude = Column("longitude", String)
