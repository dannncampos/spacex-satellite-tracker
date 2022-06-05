"""Satellite Tracker Service Layer module"""
from app.api.domain.repository.repository_satellite_tracker import RepositorySatelliteTracker
from app.api.domain.schemas.schema_satellite import SatelliteResponse


class TrackerSatellite:
    """Tracker Satellite class"""

    def __init__(self, satellite):
        self.satellite_id = satellite.satellite_id
        self.given_time = satellite.given_time
        self.repository = RepositorySatelliteTracker(self)


    def get_satellite_position(self) -> SatelliteResponse:
        """Get satellite position

        Returns:
            SatelliteResponse: The last known satellite position by a given time.
        """
        satellite_position = self.repository.get_satellite_position()

        if satellite_position:
            return SatelliteResponse(
                satellite_id = self.satellite_id,
                creation_date = satellite_position.creation_date,
                latitude = satellite_position.latitude,
                longitude = satellite_position.longitude,
            )

        return None
