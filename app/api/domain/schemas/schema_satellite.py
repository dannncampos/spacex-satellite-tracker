"""Satellite Request Module"""
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class SatelliteRequest(BaseModel):
    """This is a sample model to request a Satellite information by ID"""
    satellite_id: str = Field(..., description="The Satellite ID")
    given_time: Optional[datetime] = Field(
                                        datetime.now(),
                                        description="The given time for a last known position"
                                    )


class SatelliteResponse(BaseModel):
    """This is a sample model for Satellite Tracker response"""
    satellite_id: str
    creation_date: datetime
    latitude: float
    longitude: float


class ClosestSatelliteRequest(BaseModel):
    """This is a sample model to request the closest
    Satellite distance by a given position on a globe
    latitude, longitude coordinate and time"""

    latitude: float = Field(0.0, description="The latitude coordinate. (-90 to 90)")
    longitude: float = Field(0.0, description="The longitude coordinate. (-180 to 180")
    given_time: Optional[datetime] = Field(
                                        datetime.now(),
                                        description="The given time for a last known position"
                                    )


class ClosestSatelliteResponse(BaseModel):
    """This is a sample model for tracking
    the closest satellite response"""
    satellite_id: str
    creation_date: datetime
    latitude: float
    longitude: float
    distance: float
    unit: str
