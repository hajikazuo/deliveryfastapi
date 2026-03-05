from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///delivery.db")

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String, nullable=False)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    admin = Column(Boolean, default=False)

    def __init__(self, name, email, password, is_active=True, admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_active = is_active
        self.admin = admin

class Order(Base):
    __tablename__ = "orders"

    #ORDERS_STATUS = (
    #    ("PENDENTE", "PENDENTE"),
    #    ("CANCELADO", "CANCELADO"),
    #    ("FINALIZADO", "FINALIZADO"),
    #)

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String)
    price = Column(Float)

    def __init__(self, user_id, status="PENDENTE", price=0):
        self.user_id = user_id
        self.status = status
        self.price = price

class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_name = Column(String)
    quantity = Column(Integer)
    unitary_price = Column(Float)

    def __init__(self, order_id, product_name, quantity, unitary_price):
        self.order_id = order_id
        self.product_name = product_name
        self.quantity = quantity
        self.unitary_price = unitary_price
