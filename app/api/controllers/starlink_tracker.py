"""Controler module"""
from fastapi import APIRouter, Depends, HTTPException

from app import logger

from app.api.domain.schemas.schema_satellite import ClosestSatelliteRequest,\
                                                    ClosestSatelliteResponse,\
                                                    SatelliteRequest,\
                                                    SatelliteResponse

from app.api.service.service_satellite_tracker import TrackerSatellite
from app.api.service.service_satellite_closest import ClosestSatellite


router = APIRouter()


@router.get("/satellite/position/", response_model=SatelliteResponse)
async def get_satellite_position_by_id(request_model: SatelliteRequest = Depends()):
    """Get last known satellite position by ID

    Args:
        request_model (SatelliteResponse, optional): The ID of the satellite. Defaults to Depends().

    Raises:
        HTTPException: An exception ocurred. Satellite not found!

    Returns:
        response_model (SatelliteResponse): The last known satellite position by a given time.
    """

    logger.info("Getting last known satellite position for %s", request_model.satellite_id)

    satellite = TrackerSatellite(request_model)

    response = satellite.get_satellite_position()

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Satellite position not found"
            )

    return response


@router.get("/satellite/closest/", response_model=ClosestSatelliteResponse)
async def get_closest_satellite(request_model: ClosestSatelliteRequest = Depends()):
    """Get the closest satellite by given time and position

    Args:
        request_model (ClosestSatelliteRequest, optional):
            The given time and position on a globe as latitude and longitude coordinate.
                Defaults to Depends().

    Raises:
        HTTPException: An exception ocurred. No on satellite found for this given time!

    Returns:
        response_model (ClosestSatelliteResponse): The closest satellite information
    """

    logger.info("Getting closes satellite position for latitude %s and longitude %s",
                                    request_model.latitude, request_model.longitude)

    closest_satellite = ClosestSatellite(request_model)

    response = closest_satellite.get_closest_satellite()

    if not response:
        raise HTTPException(
            status_code=404,
            detail="Satellite not found for this given time"
            )

    return response
