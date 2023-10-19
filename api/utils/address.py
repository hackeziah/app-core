from sqlalchemy.orm import Session

from db.models.account import AddressBook
from schema.account import AddressUpdate


def get_address_book(db: Session, id: int):
    return db.query(AddressBook).filter(AddressBook.id == id).first()

def get_user_address_book(db: Session, user_id: int):
    return db.query(AddressBook).filter(AddressBook.user_id == user_id)

def get_all_address_book(db: Session, skip: int = 0, limit: int = 100):
    return db.query(AddressBook).offset(skip).limit(limit).all() 

def create_address_book(db: Session, address: AddressBook):
    db_address = AddressBook(
        full_name = address.full_name,
        contact = address.contact,
        bio = address.bio,
        full_address = address.full_address,
        barangay= address.barangay,
        city= address.city,
        district= address.district,
        region=address.region,
        postal_code= address.postal_code,
        latitude = address.latitude,
        longitude = address.longitude,
        user_id=address.user_id
        )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def update_address_book(db: Session, id: int, address: AddressBook):
    db_address = db.query(AddressBook).get(id)
    if db_address:
        db_address.full_name = address.full_name
        db_address.contact = address.contact
        db_address.bio = address.bio
        db_address.full_address = address.full_address
        db_address.barangay= address.barangay
        db_address.city= address.city
        db_address.district= address.district
        db_address.region=address.region
        db_address.postal_code= address.postal_code
        db_address.latitude = address.latitude
        db_address.longitude = address.longitude
        db.add(db_address)
        db.commit()
    db.refresh(db_address)
    return db_address


def delete_address_book(db: Session, id: int):
    db_address = db.query(AddressBook).filter(AddressBook.id == id).first()
    db.delete(db_address)
    db.commit()
    db.close()
    return True
