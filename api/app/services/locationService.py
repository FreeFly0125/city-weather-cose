from fastapi import Depends

from app.config.dbconnect import SessionLocal
from app.services.models import Location

db = SessionLocal()


def get_all():
    locations = db.query(Location).all()
    return locations


def get_one(id):
    location = db.query(Location).filter(Location.id == id).first()
    if location:
        return location.id, location.name, location.latitude, location.longitude
    else:
        return -1, "", 0, 0


def insert(name, latitude, longitude, temperature, rainfall, weather_code):
    location = Location(
        name=name,
        latitude=latitude,
        longitude=longitude,
        temperature=temperature,
        rainfall=rainfall,
        weather_code=int(weather_code),
    )

    db.add(location)
    db.commit()
    db.refresh(location)

    return location


def remove(id):
    location = db.query(Location).filter(Location.id == id).first()
    if location:
        db.delete(location)
        db.commit()
        message = "Successfully removed."
        return location.id, location.name, message
    else:
        message = "Location does not exist."
        return -1, "", message
