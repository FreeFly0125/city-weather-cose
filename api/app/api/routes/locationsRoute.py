from typing import List

from fastapi import APIRouter

from app.api.domains.locations import locationController
from app.api.domains.locations.schema import DeleteLocationRes, LocationInfoRes, NewLocationReq

locations_router = APIRouter()


@locations_router.get("/", response_model=list[LocationInfoRes])
def get_locations() -> list[LocationInfoRes]:
    result = locationController.get_all_location_info()
    all_info = [
        LocationInfoRes(id=res[0], name=res[1], temperature=res[2], rainfall=res[3], weather_code=res[4])
        for res in result
    ]
    return all_info


@locations_router.post("/", response_model=LocationInfoRes)
def new_location(payload: NewLocationReq) -> LocationInfoRes:
    res = locationController.create_location(payload.name)
    return LocationInfoRes(
        id=res.id, name=res.name, temperature=res.temperature, rainfall=res.rainfall, weather_code=res.weather_code,
    )


@locations_router.delete("/{id}", response_model=DeleteLocationRes)
def delete_location(id) -> DeleteLocationRes:
    id, name, message = locationController.delete_location(id)
    return DeleteLocationRes(
        id=id,
        name=name,
        message=message,
    )
