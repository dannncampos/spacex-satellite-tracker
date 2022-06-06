"""Load data controller module"""
from fastapi import APIRouter, Depends, HTTPException

from app import logger
from app.api.domain.schemas.schema_load_data import LoadHistoricalDataRequest,\
                                                    LoadHistoricalDataResponse
from app.api.service.convert_json_to_sql import load_data_frame_to_database


router = APIRouter()


@router.get("/load_data", response_model=LoadHistoricalDataResponse)
async def load_data(file_name: LoadHistoricalDataRequest = Depends()):
    """Load Data from a Json to MySql database

    Args:
        file_name (str): The json file name

    Raises:
        HTTPException: An exception ocurred. Something went wrong!

    Returns:
        dict: The JSON dict with the search details
    """
    load_data_frame_to_database(file_name.file)
