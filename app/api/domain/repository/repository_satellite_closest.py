"""Repository Closest Satellite Tracker module"""
from fastapi_sqlalchemy import db
from app.api.domain.models.satellite import StarlinkHistoricalData


class RepositorySatelliteClosest:
    """Repository Closest Satellite Tracker class

    Args:
        StarlinkHistoricalData (db_model): The Starlink Historical Data database model
    """

    def __init__(self, given_time):
        self.session = db.session
        self.given_time = given_time


    def get_satellites(self) -> StarlinkHistoricalData:
        """Get all satellites until given time

        Returns:
            StarlinkHistoricalData: The starlink historical data entities
        """
        query_result = self.session.query(StarlinkHistoricalData)\
            .filter(StarlinkHistoricalData.creation_date <= self.given_time)\
            .all()

        return query_result
