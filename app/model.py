import datetime
from enum import Enum

from . import db


class CatBreed(Enum):
    siberian = 'Сибирская'
    ragdoll = 'Рэгдолл'
    siamese = 'Сиамская'
    british_shorthair = 'Британская короткошерстная'
    american_shorthair = 'Американская короткошерстная'
    scottish_lop_eared = 'Шотландская вислоухая'
    bombay = 'Бомбейский'
    persian = 'Персидская'
    maine_coon = 'Мейн-кун'
    bengal = 'Бенгальская'


class Cat(db.Model):

    __tablename__ = "cat"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    dob = db.Column(db.Date, nullable=False)
    breed = db.Column(db.Enum(CatBreed), nullable=False)
    image_url = db.Column(db.String(255))
    description = db.Column(db.Text)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def age_in_months(self):
        return round((datetime.date.today() - self.dob).days / 30)

    def __repr__(self):
        return f"<Cat id={self.id}, name={self.name}, breed={self.breed}>"
