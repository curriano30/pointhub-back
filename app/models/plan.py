from sqlalchemy import Column, Integer,Numeric, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class Plan(Base):
    __tablename__ = "plans"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Numeric, nullable=False)

    # Relación con Subscription
    subscriptions = relationship('Subscription', back_populates='plan')