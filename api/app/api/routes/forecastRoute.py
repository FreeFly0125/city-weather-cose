from fastapi import APIRouter

from app.api.domains.forecast.forecastController import get_weekly_forecast_info
from app.api.domains.forecast.schema import DailyForecast, WeeklyForecast

forecast_router = APIRouter()


@forecast_router.get("/{id}")
def get_forecast(id) -> WeeklyForecast | str:
    name, country, info = get_weekly_forecast_info(id)
    if len(info) == 0:
        return "Not Found"

    forecast_info = WeeklyForecast(
        name=name,
        country=country,
        forecast=[
            DailyForecast(
                date=finfo[0], day=finfo[1], weather_code=finfo[2], min_temperature=finfo[3], max_temperature=finfo[4],
            )
            for finfo in info
        ],
    )

    return forecast_info
