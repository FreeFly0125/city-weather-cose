from app.consts.location_info import locationDetail
from app.services import locationService, openmeteo


def get_all_location_info():
    all_detail = locationService.get_all()
    all_info = [[rinfo.id, rinfo.name, rinfo.temperature, rinfo.rainfall, rinfo.weather_code] for rinfo in all_detail]
    return all_info


def create_location(name: str):
    [_, latitude, longitude] = locationDetail.data[name]

    weather_info = openmeteo.get_current_weather(latitude, longitude)

    result = locationService.insert(
        name, latitude, longitude, weather_info(0).Value(), weather_info(1).Value(), weather_info(2).Value(),
    )

    return result


def delete_location(id: int):
    return locationService.remove(id)
