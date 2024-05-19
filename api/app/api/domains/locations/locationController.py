from app.services import locationService


def get_all_location_info():
    all_detail = locationService.get_all()
    all_info = [[rinfo.id, rinfo.name, rinfo.temperature, rinfo.rainfall, rinfo.weather_code] for rinfo in all_detail]
    return all_info
