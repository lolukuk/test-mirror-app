from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas
import datetime


def get_orders_by_date(db: Session, date: datetime):
    return db.execute(select(models.Order).where(models.Order.walk_date == date.date())).scalars().all()


def create_order(db: Session, order: schemas.OrderCreate):
    existing_order = db.execute(
        select(models.Order).where(
            models.Order.walk_date == order.walk_date.date(),
            models.Order.walk_time == order.walk_time,
            models.Order.walker == order.walker
        )
    ).scalars().first()

    if existing_order:
        return None

    db_order = models.Order(
        apartment_number=order.apartment_number,
        pet_name=order.pet_name,
        pet_breed=order.pet_breed,
        walk_date=order.walk_date.date(),
        walk_time=order.walk_time,
        walker=order.walker
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
