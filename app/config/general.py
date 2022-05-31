"""Environment configuration"""
from os import getenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application environment configuration"""
    TABLE = getenv('MYSQL_TABLE')
    HOST = getenv('MYSQL_HOST')
    DATABASE = getenv('MYSQL_DATABASE')
    PORT = getenv('MYSQL_PORT')
    USER = getenv('MYSQL_USER')
    PASSWORD = getenv('MYSQL_PASSWORD')
    TABLE_INDEX = getenv('MYSQL_TABLE_INDEX')
    DATA_FOLDER = getenv('DATA_FOLDER')


settings = Settings()
