"""Closest Position Service Layer module"""
from haversine import haversine, Unit
from app.api.domain.repository.repository_satellite_closest import RepositorySatelliteClosest
from app.api.domain.schemas.schema_satellite import ClosestSatelliteResponse


class ClosestSatellite:
    """Closest Satellite class"""

    def __init__(self, request_closest):
        self.latitude = request_closest.latitude
        self.longitude = request_closest.longitude
        self.given_time = request_closest.given_time
        self.repository = RepositorySatelliteClosest(self.given_time)


    @classmethod
    def calculate_closest_satellite(cls, satellites: list, this_point: tuple, unit: Unit)\
                                                -> tuple[list, float]:
        """Calculate the minimum distance from a given point

        Args:
            satellites (list): All satellites launch information
            this_point (tuple): The given point coordinate Latitude and longitude
            unit (tuple): Haversine unit

        Returns:
            tuple[list, float]: The closest satellite
                            and the minimum distance of the closest satellite
        """
        minimum_distance = None

        for satellite in satellites:
            satellite_distance =  haversine(
                (satellite.latitude or 0, satellite.longitude), this_point, unit=unit)

            if not minimum_distance or satellite_distance < minimum_distance:
                minimum_distance = satellite_distance
                closest_satellite = satellite

        return closest_satellite, minimum_distance


    def get_closest_satellite(self) -> ClosestSatelliteResponse:
        """Get closest satellite

        Returns:
            ClosestSatelliteResponse: The closest satellite position by a given time and coordinate.
        """
        haversine_unit = Unit.MILES

        satellites = self.repository.get_satellites()

        closest_satellite, minimum_distance = self.calculate_closest_satellite(satellites,
                                                (self.latitude, self.longitude), haversine_unit)

        if closest_satellite:
            return ClosestSatelliteResponse(
                    satellite_id = closest_satellite.satellite_id,
                    creation_date = closest_satellite.creation_date,
                    latitude = closest_satellite.latitude,
                    longitude = closest_satellite.longitude,
                    given_latitude = self.latitude,
                    given_longitude = self.longitude,
                    given_time = self.given_time,
                    distance = minimum_distance,
                    unit = haversine_unit.name,
            )

        return None
