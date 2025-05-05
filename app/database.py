from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
import psycopg2
from urllib.parse import quote_plus

load_dotenv()


# sqlite = os.environ.get('CONTRATANTE')

# # Para usar SQLite (arquivo local)
# DATABASE_URL = f'sqlite:///./{sqlite}.db'

# Para usar as váriaveis de ambiente, coloque as informações que estão de exemplo no arquivo env_exemplo/ dentro de um arquivo .env/

# Obtém as configurações do banco de dados através das variáveis de ambiente
usuario = quote_plus(os.environ.get('USUARIO'))
senha = quote_plus(os.environ.get('SENHA'))
banco = os.environ.get('BANCO')
ambiente = os.environ.get('AMBIENTE')
porta = os.environ.get('PORTA')

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
