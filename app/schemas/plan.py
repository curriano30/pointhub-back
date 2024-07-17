from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    price_monthly = Column(Integer, nullable=False)
    discount_annual = Column(Integer, nullable=False)  # Discount for annual payment in percentage
    max_clients = Column(Integer, nullable=False)
    max_locations = Column(Integer, nullable=False)
    support = Column(String, nullable=False)

    # Relationship with users
    users = relationship('User', back_populates='plan')