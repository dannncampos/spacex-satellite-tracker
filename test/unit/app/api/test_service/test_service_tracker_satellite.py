"""Test Tracker Satellite"""
from datetime import datetime
import pytest

from app.api.service.service_tracker_satellite import TrackerSatellite
from test import tools_for_testing


@pytest.mark.parametrize(
    "satellite_id, creation_date, expected",
    [
        ("5eed770f096e590006985613", datetime(2022, 1, 26, 13, 26, 11), ["14", "-24.712922471107795")
    ]
)
def test_get_satellite_by_id(satellite_id: str, creation_date: datetime, expected: list):
    """Test method get satellite by id

    Args:
        satellite_id (str): The satellite ID from Spacex launch
        creation_date (date): The creation date
        expected (list): The expected result
    """
    tools_for_testing.check_return(
        TrackerSatellite(satellite_id).get_satellite_by_id(creation_date),
        expected
    )



