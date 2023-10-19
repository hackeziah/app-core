import fastapi

from typing import List
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from schema.account import User, UserCreate

from api.utils.users import get_users, get_user_by_email, create_user, get_user

router =  fastapi.APIRouter()

@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users", response_model=User, status_code=201)
async def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email is already exists")
    return create_user(db=db, user=user)


@router.get("/users/{id}", response_model=User)
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, id=id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user