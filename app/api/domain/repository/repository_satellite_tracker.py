"""Repository Satellite Tracker module"""
from fastapi_sqlalchemy import db
from sqlalchemy import and_

from app.api.domain.models.satellite import StarlinkHistoricalData


class RepositorySatelliteTracker(StarlinkHistoricalData):
    """Repository Satellite Tracker class

    Args:
        StarlinkHistoricalData (db_model): The Starlink Historical Data database model
    """

    def __init__(self, args):
        self.session = db.session
        self.satellite_id = args.satellite_id
        self.creation_date = args.given_time


    def get_satellite_position(self) -> StarlinkHistoricalData:
        """Get satellite position by ID on a given time

        Returns:
            StarlinkHistoricalData: The starlink historical data entity
        """
        query_result = self.session.query(StarlinkHistoricalData)\
            .filter(
                and_(
                    StarlinkHistoricalData.satellite_id == self.satellite_id,
                    StarlinkHistoricalData.creation_date <= self.creation_date))\
            .order_by(StarlinkHistoricalData.creation_date.desc())\
            .first()

        return query_result
