# app-core
Simple CRUD FASTAPI with Geo Search 

Hi to try my application
Please do the following:
   - git clone the repo
   > If no virtual env 
      - Create virtual environment Command: (python -m venv venv)
      - Activate the virtual environment
         Command: venv\Scripts\activate
         Command LINUX: source venv\Scripts\activate
         - Install the packages using PIP Command: pip install -r requirements.txt
   > If you want to clean the database do the following:
      - Delete the (address_book.db)   
   > Delete the file in revision folder (pycache and .py)
   - Then RUN "alembic revision --autogenerate" to generate new migration   
   - Then RUN the project using: "uvicorn main:app"

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
