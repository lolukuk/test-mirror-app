from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud, db
import datetime

# Инициализация FastAPI
app = FastAPI()

# Создание таблиц
models.Base.metadata.create_all(bind=db.engine)


# 1. Вывод заказов на указанную дату
@app.get("/orders/", response_model=list[schemas.OrderCreate])
def get_orders(date: datetime, db: Session = Depends(db.get_db)):
    orders = crud.get_orders_by_date(db, date)
    return orders


# 2. Оформление заказа
@app.post("/orders/", response_model=schemas.OrderCreate)
def create_order(order: schemas.OrderCreate, db: Session = Depends(db.get_db)):
    db_order = crud.create_order(db, order)
    if db_order is None:
        raise HTTPException(status_code=400, detail="Уже существует заказ на это время для данного выгуливающего.")
    return db_order


def main():
    pass


if __name__ == '__main__':
    main()
