from sqlalchemy import Column, Float, Integer, String
from .database import Base


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    colour = Column(String(30))
    weight = Column(Float)
    price = Column(Float)
    name = Column(String(64), nullable=True)

    def __init__(self, colour, weight, price, name=None):
        self.colour = colour
        self.weight = weight
        self.price = price
        self.name = name

    def __repr__(self):
        return f'Product {self.name}, colour: {self.colour}, weight: {self.weight}, price: {self.price}'


class Address(Base):
    __tablename__ = 'addresses'

    address_id = Column(Integer, primary_key=True)
    country = Column(String(64))
    city = Column(String(64))
    street = Column(String(64))
    house_number = Column(Integer)

    def __init__(self, country, city, street, house_number):
        self.country = country
        self.city = city
        self.street = street
        self.house_number = house_number

    def __repr__(self):
        return f'Address: {self.country}, {self.city}, {self.street}, {self.house_number}'