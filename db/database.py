from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
  
from config import Settings

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/dbname"
import os
postgres_user: str = os.environ.get("POSTGRES_USER")  
postgres_password: str = os.environ.get("POSTGRES_PASSWORD")  
postgres_server: str = os.environ.get("POSTGRES_SERVER")  
postgres_port: str = os.environ.get("POSTGRES_PORT")
postgres_db: str = os.environ.get("POSTGRES_DB")  
db_echo_log: bool = True if os.environ.get("DEBUG") == "True" else False

database_url = Settings(postgres_user, postgres_password, postgres_server, postgres_port, postgres_db)

# engine = create_engine(database_url.sync_database_url)
# POSTGRES_USER="postgres"  
# POSTGRES_PASSWORD="postgres"  
# POSTGRES_SERVER="db_postgres"  
# POSTGRES_PORT=5432
# POSTGRES_DB="postgres"
# PGADMIN_EMAIL="admin@admin.com"
# PGADMIN_PASSWORD="admin"
#  DB_DATABASE=coredb
# DB_PORT=3306
# DB_USERNAME=admin
# DB_PASSWORD=password

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/core_dbase"
engine = create_engine(database_url.sync_database_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()