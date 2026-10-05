"""SQLAlchemy models - auto-generated."""
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Text
from datetime import datetime
from database import Base

class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
