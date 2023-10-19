# app-core
![image](https://github.com/hackeziah/app-core/assets/21010227/e2d404dd-de25-433e-961e-1e954a08268f)

Simple CRUD FASTAPI with Geo Search 

Hi to try my application
Please do the following:
   - git clone the repo
   If no virtual env 
      1. Create virtual environment Command: (python -m venv venv)
      2. Activate the virtual environment
         Command: venv\Scripts\activate
         Command LINUX: source venv/Scripts/activate
      3. Install the packages using PIP Command: pip install -r requirements.txt
   - If you want to clean the database do the following:
      1. Delete the (address_book.db)
      2. Delete the file in the revision folder (pycache and .py)
      3. Then RUN "alembic revision --autogenerate" to generate new migration   
   - Then RUN the project using: "uvicorn main:app"

   - GO to http://127.0.0.1:8000/docs

Technology use: 
   - FastAPI
   - Alembic
   - Sqlalchemy
   - Geopy (Maps Nominatim) 

For Future Task:
  - Doc String
  - Add Logging
  - Pytest

References:
   - https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/
   - https://fastapi.tiangolo.com/
   - https://alembic.sqlalchemy.org/en/latest/autogenerate.html
   - https://geopy.readthedocs.io/en/stable/
