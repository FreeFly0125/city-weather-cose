from sqlalchemy import Column, Float, Integer, String

from app.config.dbconnect import Base, engine


class Location(Base):
    __tablename__ = "Location"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    temperature = Column(Float, nullable=True)
    rainfall = Column(Float, nullable=True)
    weather_code = Column(Integer, nullable=True)


Base.metadata.create_all(bind=engine)
