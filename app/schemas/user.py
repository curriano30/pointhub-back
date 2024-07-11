from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class UserType(enum.Enum):
    consumer = "consumer"
    company = "company"

class UserRole(enum.Enum):
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
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=True)

    company = relationship("Company", back_populates="users")
