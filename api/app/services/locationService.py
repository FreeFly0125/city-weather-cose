from app.config.dbconnect import SessionLocal
from app.services.models import Location

db = SessionLocal()


def get_all():
    locations = db.query(Location).all()
    return locations