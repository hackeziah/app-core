class Settings:
    def __init__(self, postgres_user, postgres_password, postgres_server, postgres_port, postgres_db):
        self.postgres_user = postgres_user
        self.postgres_password = postgres_password
        self.postgres_server = postgres_server
        self.postgres_port = postgres_port
        self.postgres_db = postgres_db


    @property  
    def sync_database_url(self) -> str:  
        # return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_server}:{self.postgres_port}/{self.postgres_db}"
        return "postgresql://postgres:postgres@db:5432/core_dbase"
    
    "postgresql://postgres:postgres@db:5432/core_dbase"