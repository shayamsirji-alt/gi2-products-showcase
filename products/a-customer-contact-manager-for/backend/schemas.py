"""Pydantic schemas - auto-generated."""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ContactBase(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True
