from datetime import date
from typing import List

from pydantic import BaseModel


class DailyForecast(BaseModel):
    date: date
    day: str
    weather_code: int
    min_temperature: float
    max_temperature: float


class WeeklyForecast(BaseModel):
    name: str
    country: str
    forecast: list[DailyForecast]
