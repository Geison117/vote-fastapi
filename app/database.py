from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg
import time
from .config import settings

#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:1234@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#while True:
#    try:
#        conn = psycopg.connect(host='localhost', 
#                               dbname='fastapi', 
#                               user='postgres', 
#                               password='1234', 
#                               row_factory=psycopg.rows.dict_row)
#
#        cursor = conn.cursor()
#        print("Database connection was successful")
#        break
#    except Exception as error:
#        print("Connecting to database failed")    
#        print("Error: ", error)
#        time.sleep(2)                        
