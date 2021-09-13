from typing import Generator, List
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Query
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

class MyQuery(Query) : 

    def pagination(self, 
                    page:int=1,
                    per_page:int=1,
                    max_per_page:int=1,
                    count:int=0) -> List:
        items = self.limit(per_page).offset((page-1)*per_page).all()
        
        return items


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine,query_cls=MyQuery)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
   
