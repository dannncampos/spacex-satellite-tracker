"""Satellite Request Module"""
from typing import Optional
from pydantic import BaseModel, Field


class HellowWorldRequest(BaseModel):
    """This is a sample model to request a HellowWorld"""
    hellow_world_id: str = Field(..., description='Hellow World ID')


class HellowWorldResponse(BaseModel):
    """This is a sample model for HellowWorld response"""
    hellow_world_id: str
    hellow_world_msg: str
    is_hellow_world: bool
