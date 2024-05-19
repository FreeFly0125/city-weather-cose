from fastapi import APIRouter

from .forecastRoute import forecast_router
from .locationsRoute import locations_router

api_router = APIRouter()

api_router.include_router(locations_router, prefix="/locations")
api_router.include_router(forecast_router, prefix="/forecast")
