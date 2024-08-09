from pydantic import BaseModel, constr, conint, validator
from datetime import time, datetime


class OrderCreate(BaseModel):
    apartment_number: conint(gt=0)
    pet_name: str
    pet_breed: str
    walk_date: datetime
    walk_time: time
    walker: constr(regex="^(Пётр|Антон)$")

    @validator("walk_time")
    def validate_walk_time(cls, v):
        if v.minute not in (0, 30):
            raise ValueError("Прогулка может начинаться только в начале часа или в половину.")
        if not (time(7, 0) <= v <= time(23, 0)):
            raise ValueError("Прогулка должна начинаться не ранее 7:00 и не позднее 23:00.")
        return v
