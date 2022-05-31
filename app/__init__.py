"""Module App"""
import logging
from logging.config import dictConfig
from sqlalchemy.ext.declarative import declarative_base

from app.config.logging import LogConfig 
from app.config.general import settings


dictConfig(LogConfig().dict())

logger = logging.getLogger("fastapi")

Base = declarative_base()
