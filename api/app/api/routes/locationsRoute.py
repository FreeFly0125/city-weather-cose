from typing import List

from fastapi import APIRouter

from app.api.domains.locations import locationController
from app.api.domains.locations.schema import LocationInfoRes

locations_router = APIRouter()


@locations_router.get("/", response_model=list[LocationInfoRes])
def get_locations() -> list[LocationInfoRes]:
    result = locationController.get_all_location_info()
    all_info = [
        LocationInfoRes(id=res[0], name=res[1], temperature=res[2], rainfall=res[3], weather_code=res[4])
        for res in result
    ]
    return all_info
