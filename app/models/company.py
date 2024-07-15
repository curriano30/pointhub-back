from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Company(Base):
    __tablename__ = "companies"  # Corregido el nombre de la tabla a "companies"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)

    # Relación con los empleados (usuarios)
    employees = relationship('User', back_populates='company', cascade='all, delete-orphan')
