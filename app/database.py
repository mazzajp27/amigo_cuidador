from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
import psycopg2
from urllib.parse import quote_plus

load_dotenv()

# Para usar SQLite (arquivo local)
DATABASE_URL = os.getenv("sqlite")


# Se depois quiser trocar para PostgreSQL, é só comentar o de cima e descomentar esse:

DATABASE_URL = f'postgresql://{usuario}:{senha}@{ambiente}:{porta}/{banco}'
# DATABASE_URL = 'postgresql://postgres:Apex123.@localhost:5432/contratante'


# # # Criação do engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# DATABASE_URL = 'postgresql://postgres:Apex123.@localhost:5432/contratante'

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
# Base = declarative_base()
