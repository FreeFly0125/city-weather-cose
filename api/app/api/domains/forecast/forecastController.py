import datetime

from app.consts.location_info import locationDetail
from app.services import locationService
from app.services.openmeteo import get_weekly_forecast


def get_weekly_forecast_info(location_id):
    id, name, latitude, longitude = locationService.get_one(location_id)
    if id == -1:
        return name, []
    
    country = locationDetail.data[name][0]

    forecast_info = get_weekly_forecast(latitude=latitude, longitude=longitude)

    weather_code = forecast_info(0).ValuesAsNumpy()
    min_temperature = forecast_info(1).ValuesAsNumpy()
    max_temperature = forecast_info(2).ValuesAsNumpy()

    response = []
    today = datetime.date.today()

    for i in range(7):
        date = today + datetime.timedelta(days=i)
        response.append([date, date.strftime("%a"), int(weather_code[i]), min_temperature[i], max_temperature[i]])

    return name, country, response
