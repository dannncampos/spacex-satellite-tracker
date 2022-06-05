"""Test Tracker Satellite"""
from test import tools_for_testing
from datetime import datetime

import pytest

from api.domain.schemas.schema_satellite import SatelliteRequest, SatelliteResponse
from app.api.service.service_satellite_tracker  import TrackerSatellite


@pytest.mark.parametrize(
    "input_test, expected",
    [
        (
            SatelliteRequest(
              satellite_id = "5eed770f096e590006985613",
              given_time = datetime(2022, 6, 5, 13, 26, 11)
          ),
            SatelliteResponse(
                satellite_id = "5eed770f096e590006985613",
                creation_date = datetime(2022, 1, 26, 13, 26, 11),
                latitude = -24.7129,
                longitude = 14,
            )
        )
    ]
)
def test_get_satellite_position(input_test: SatelliteRequest, expected: SatelliteResponse):
    """Test method get last known satellite position

    Args:
        input_test (SatelliteRequest): The satellite ID from Spacex launch for a given time
        expected (SatelliteResponse): The last known position of a satellite by ID
    """
    result = TrackerSatellite(input_test).get_satellite_position()

    tools_for_testing.check_return(result, expected)
