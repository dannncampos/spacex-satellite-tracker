"""Load data Request Module"""
from typing import Optional
from pydantic import BaseModel, Field


class LoadHistoricalDataRequest(BaseModel):
    """Load Historical Data Request Class"""
    file: str = Field(..., description='Load a Json file')


class LoadHistoricalDataResponse(BaseModel):
    """Load Historical Data Response Class"""
    file: str
