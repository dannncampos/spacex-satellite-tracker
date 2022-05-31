"""Controler module"""
from fastapi import APIRouter, Depends, HTTPException

from app import logger
from app.api.domain.schemas.schema_satellite import HellowWorldRequest, \
                                                HellowWorldResponse
from app.api.service.service_sample import get_hellow_world



router = APIRouter()

ID = {"01": {"teste"}}


@router.get("/satellite/{id}")
async def get_satellite_by_id(id: str):
    """Get satellite ID from BD

    Args:
        id (str): The ID of the satellite

    Raises:
        HTTPException: An exception ocurred. Something went wrong!

    Returns:
        dict: The JSON dict with the search details
    """

    if id not in ID:
        raise HTTPException(
            status_code=404,
            detail="Satellite ID not found"
            )

    return {"satellite": ID[id]}
