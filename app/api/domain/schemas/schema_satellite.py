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
