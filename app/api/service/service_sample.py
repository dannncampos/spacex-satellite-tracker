"""Sample Service Layer module"""
from app.api.domain.repository import repository_sample
from app.api.domain.models.satellite import StarlinkHistoricalData
from app.api.domain.schemas.schema_satellite import HellowWorldResponse, HellowWorldRequest


def get_hellow_world(hellow_world: HellowWorldRequest):

    response = HellowWorldResponse(
        hellow_world_id=hellow_world.hellow_world_id,
        hellow_world_msg="Hellow World",
        is_hellow_world=True
    )

    return response
