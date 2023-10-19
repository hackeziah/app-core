from datetime import datetime

from pydantic import BaseModel
from typing import List, Optional


class BaseModel(BaseModel):
    created_at: datetime
    updated_at: datetime


class User(BaseModel):
    id: int
    email: str
    is_active: bool


class UserCreate(User):
    email: str
    is_active: bool


class Address(BaseModel):
    id: int
    full_name: str
    contact: str
    bio: str
    full_address: str
    barangay: str
    city: str
    district: str
    region: str
    postal_code: str
    latitude : float
    longitude: float


class AddressCreate(BaseModel):
    full_name: str
    contact: str
    bio: str
    full_address: str
    barangay: str
    city: str
    district: str
    region: str
    postal_code: str
    latitude : float
    longitude: float
    user_id: int


class AddressUpdate(BaseModel):
    full_name: str
    contact: str
    bio: str
    full_address: str
    barangay: str
    city: str
    district: str
    region: str
    postal_code: str
    latitude : float
    longitude: float