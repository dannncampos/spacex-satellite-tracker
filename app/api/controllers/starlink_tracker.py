"""Controler module"""
from fastapi import APIRouter, Depends, HTTPException

from app import logger
from app.api.domain.schemas.schema_satellite import SatelliteRequest,\
                                                    SatelliteResponse
from app.api.service.service_satellite_tracker import TrackerSatellite


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
