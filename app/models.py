from sqlalchemy import Column, Integer, String, Date, Time
from .db import Base


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    apartment_number = Column(Integer, nullable=False)
    pet_name = Column(String, nullable=False)
    pet_breed = Column(String, nullable=False)
    walk_date = Column(Date, nullable=False)
    walk_time = Column(Time, nullable=False)
    walker = Column(String, nullable=False)
