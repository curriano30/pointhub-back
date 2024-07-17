from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class UserRole(enum.Enum):
    admin = "admin"
    employee = "employee"

class Local(Base):
    __tablename__ = "locals"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True, nullable=False)
    address = Column(String, nullable=False)
    contact_email = Column(String, unique=True, index=True, nullable=True)
    contact_phone = Column(String, nullable=True)
    creator_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    manager_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    # Relationship with users
    creator = relationship('User', foreign_keys=[creator_id], back_populates='created_locals')
    manager = relationship('User', foreign_keys=[manager_id])
    employees = relationship('LocalEmployee', back_populates='local')

class LocalEmployee(Base):
    __tablename__ = "local_employees"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    local_id = Column(Integer, ForeignKey('locals.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    # Relationship with local and user
    local = relationship('Local', back_populates='employees')
    user = relationship('User', back_populates='local_employee')
