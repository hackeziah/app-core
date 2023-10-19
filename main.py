import uvicorn

from api import address, users
from fastapi import FastAPI

from db.database import engine
from db.models import account

account.Base.metadata.create_all(bind=engine)


description = """
Address Book API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
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


app.include_router(users.router)
app.include_router(address.router)