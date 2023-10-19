import fastapi

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List
from db.database import get_db
from schema.account import Address, AddressCreate, AddressUpdate

from geopy.geocoders import Nominatim
from api.utils.users import get_user
from api.utils.address import (
    create_address_book,
    delete_address_book,
    update_address_book,
    get_all_address_book,
    get_user_address_book,
    get_address_book,
    
)

geolocator = Nominatim(user_agent="geopy-example")

router =  fastapi.APIRouter()


@router.get("/find-address-by-location")
async def get_address_by_location(latitude:float, longitude: float):
    location = geolocator.reverse((latitude, longitude), exactly_one=True, language='en')
    if not location:
        raise HTTPException(status_code=404, detail="Address not found.")

    location_data = {
        'full_address' : str(location.raw['display_name']),
        'barangay' : str(location.raw['address']['quarter']) if location.raw['address'].get("quarter", "")  else "",
        'city' : str(location.raw['address']['city']) if location.raw['address'].get("city", "") else "",
        'district': str(location.raw['address']['state_district']) if location.raw['address'].get("state_district", "") else "",
        'region':  str(location.raw['address']['region']) if location.raw['address'].get("region", "")  else "",
        'postal_code':  str(location.raw['address']['postcode']) if location.raw['address'].get("postcode", "")  else "",
        'latitude' : float(location.raw['lat']) if location.raw['lat'] else "",
        'longitude' : float(location.raw['lon']) if location.raw['lon'] else "",
    }
    	
    return location_data


@router.get("/search-address/{address_name}")
async def get_address_by_name(address_name):
    location_item = geolocator.geocode(address_name, country_codes='PH')
    if not location_item:
        raise HTTPException(status_code=404, detail="Address not found. Please make more specific.")
    
    location = geolocator.reverse((location_item.raw['lat'], location_item.raw['lon']), exactly_one=True, language='en')
    
    if not location:
        raise HTTPException(status_code=404, detail="Address not found.")
    
    location_data = {
        'full_address' : str(location.raw['display_name']),
        'barangay' : str(location.raw['address']['quarter']) if location.raw['address'].get("quarter", "")  else "",
        'city' : str(location.raw['address']['city']) if location.raw['address'].get("city", "") else "",
        'district': str(location.raw['address']['state_district']) if location.raw['address'].get("state_district", "") else "",
        'region':  str(location.raw['address']['region']) if location.raw['address'].get("region", "")  else "",
        'postal_code':  str(location.raw['address']['postcode']) if location.raw['address'].get("postcode", "")  else "",
        'latitude' : float(location.raw['lat']) if location.raw['lat'] else "",
        'longitude' : float(location.raw['lon']) if location.raw['lon'] else "",
    }
    	
    return location_data


@router.post("/address-book", response_model=Address, status_code=201)
async def create_new_address_book(address: AddressCreate, db: Session = Depends(get_db)):
    db_user = get_user(db=db, id=address.user_id)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not exist")
    return create_address_book(db=db, address=address)

@router.get("/address-book", response_model=List[Address])
async def get_all_address(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_all_address_book(db, skip=skip, limit=limit)
    return users

@router.get("/address-book/{id}", response_model=Address)
async def get_address_by_id(id: int, db: Session = Depends(get_db)):
    address = get_address_book(db=db, id=id)
    if not address:
        raise HTTPException(status_code=400, detail="Not Found")
    return address

@router.get("/address-book/{user_id}", response_model=List[Address])
async def get_address_by_user_id(user_id: int, db: Session = Depends(get_db)):
    address = get_user_address_book(db=db, user_id=user_id)
    if not address:
        raise HTTPException(status_code=400, detail="Not Found")
    return address

@router.put("/address-book/{id}", response_model=Address)
def update_address_book_by_id(id: int, address: AddressUpdate,  db: Session = Depends(get_db)):
    address = get_address_book(db=db, id=id)
    if not address:
        raise HTTPException(status_code=400, detail="Address Book Not Found")
    update_address = update_address_book(db=db, id=id, address=address)
    return update_address

@router.delete("/address-book/{id}", status_code=204)
def delete_address_book_by_id(id: int,  db: Session = Depends(get_db)):
    address = get_address_book(db=db, id=id)
    if not address:
        raise HTTPException(status_code=400, detail="Address Book Not Found")
    delete_address_book(db=db, id=id)
    return None