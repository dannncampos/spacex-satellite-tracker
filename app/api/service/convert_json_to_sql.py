import json
import pandas as pd
import sqlalchemy

from app.config.db import engine
from app.config.general import settings


def read_json_to_data_frame(file_path):
    with open(file_path) as f:
        data = json.load(f)

    df = pd.json_normalize(data)
    df.columns = df.columns.str.replace('.', '_').str.lower()
    df.drop(df.columns.difference(['spacetrack_creation_date',
                                    'longitude',
                                    'latitude',
                                    'id']), 1, inplace=True)

    return df


def load_data_frame_to_database(file_path: str):
    file_path = settings.DATA_FOLDER+file_path

    return read_json_to_data_frame(file_path).to_sql(settings.TABLE,
                                    con=engine,
                                    index=True,
                                    if_exists='replace',
                                    index_label=settings.TABLE_INDEX,
                                    dtype={'spacetrack_creation_date': sqlalchemy.DateTime(),
                                    'longitude': sqlalchemy.types.Float(precision=3, asdecimal=True),
                                    'latitude': sqlalchemy.types.Float(precision=3, asdecimal=True),
                                    'id': sqlalchemy.types.VARCHAR(length=255)})
