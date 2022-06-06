"""Logging configuration"""
from logging import handlers
from pydantic import BaseModel


class LogConfig(BaseModel):
    """Logging configuration Class"""

    logger_name: str = "fastapi"
    log_format: str = "%(asctime)s - %(message)s"
    log_level: str = "DEBUG"

    version = 1
    disable_existing_loggers = False

    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": log_format,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }

    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr"
        }
    }

    loggers = {
        "fastapi": {
            "handlers": ["default"],
            "level": log_level
        }
    }
