from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("User_DataBase")
DB_PASSWORD = os.getenv("Password_DataBase")
DB_HOST = os.getenv("Host_DataBase")
DB_PORT = os.getenv("Port_DataBase")
DB_NAME = os.getenv("Name_DataBase")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
