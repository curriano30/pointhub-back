from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, Enum, Numeric
from sqlalchemy.orm import relationship
from app.db.base import Base
from datetime import datetime, timezone
import enum

class PaymentInterval(enum.Enum):
    monthly = "monthly"
    annual = "annual"
class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    plan_id = Column(Integer, ForeignKey('plans.id'), nullable=False)
    start_date = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    end_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    payment_interval = Column(Enum(PaymentInterval), nullable=False)
    amount = Column(Numeric, nullable=False)
    auto_renew = Column(Boolean, default=True, nullable=False)

    # Relación con User y Plan
    user = relationship('User', back_populates='subscriptions')
    plan = relationship('Plan', back_populates='subscriptions')