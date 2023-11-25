import uvicorn

from api import address, users
from fastapi import FastAPI
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware






from db.database import engine
from db.models import account

account.Base.metadata.create_all(bind=engine)


description = """
Address Book API helps you do awesome stuff. 🚀

* **Create users**
* **Read users** 
* **Find address using lat and long** 
* **Find address using address name**
* **CRUD for AddressBook**  

"""
app = FastAPI(
    title="Address Book API",
    description=description,
    summary="Address Book API",
    version="0.0.1",
    contact={
        "name": "Kevin Paul Lamadrid",
        "email": "lamadridkevinpaul@gmail.com",
    },
    license_info={
        "name": "ABAPI 1.0",
    },
)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(address.router)