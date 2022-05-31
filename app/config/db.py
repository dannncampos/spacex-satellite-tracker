from sqlalchemy import create_engine
from app.config.general import settings


connection_str = f"mysql+pymysql://{settings.USER}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.DATABASE}"
engine = create_engine(connection_str)
conn = engine.connect()
