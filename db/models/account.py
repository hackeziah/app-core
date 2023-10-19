from sqlalchemy import Boolean, Column, Integer, ForeignKey, Float, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from ..database import Base
from ..models.base import Timestamp


class User(Timestamp, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    is_active = Column(Boolean, default=False)
    
    address = relationship("AddressBook", back_populates="owner", uselist=False)


class AddressBook(Timestamp, Base):
    __tablename__ = "address_book"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=False)
    contact = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    full_address = Column(Text, nullable=False) 
    barangay= Column(String(50), nullable=True)
    city= Column(String(25), nullable=True)
    district= Column(String(20), nullable=True)
    region=Column(String(50), nullable=True)
    postal_code= Column(String(10), nullable=True)
    latitude  =  Column(Float)
    longitude =  Column(Float)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="address")