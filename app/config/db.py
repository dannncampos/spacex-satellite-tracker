from sqlalchemy import create_engine
from app.config.general import settings


engine = create_engine(settings.CONNECTION_STR)
conn = engine.connect()
