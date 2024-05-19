from typing import List

from pydantic import BaseModel


class LocationInfoRes(BaseModel):
    id: int
    name: str
    temperature: float
    rainfall: float
    weather_code: int


class NewLocationReq(BaseModel):
    name: str


class DeleteLocationRes(BaseModel):
    id: int
    name: str
    message: str
