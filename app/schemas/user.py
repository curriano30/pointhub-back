from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class UserType(enum.Enum):
    consumer = "consumer"
    company = "company"

class UserRole(enum.Enum):
    creator = "creator"
    admin = "admin"
    employee = "employee"

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_verified = Column(Boolean, default=False)
    type = Column(Enum(UserType), nullable=False)
    role = Column(Enum(UserRole), nullable=True)
    plan_id = Column(Integer, ForeignKey('plans.id', ondelete='CASCADE'), nullable=True)

    # Relación con el plan
    plan = relationship('Plan', back_populates='users')

    # Relación con los locales creados y empleados
    created_locals = relationship('Local', back_populates='creator')
    local_employee = relationship('LocalEmployee', back_populates='user')