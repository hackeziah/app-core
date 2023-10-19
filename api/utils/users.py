from sqlalchemy.orm import Session

from db.models.account import User


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all() 

def create_user(db: Session, user: User):
    db_user = User(email=user.email, is_active=user.is_active)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
