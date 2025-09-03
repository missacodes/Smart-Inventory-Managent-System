from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    sku = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    category = Column(String)
    unit_cost = Column(Numeric(10, 2))
    unit_price = Column(Numeric(10, 2))

class Store(Base):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    region = Column(String)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey("stores.store_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    on_hand = Column(Integer, default=0)
    on_order = Column(Integer, default=0)
    reserved = Column(Integer, default=0)
    updated_at = Column(TIMESTAMP)

    product = relationship("Product")
    store = relationship("Store")
