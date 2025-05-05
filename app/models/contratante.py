from sqlalchemy import Column, Integer, String, Float, Numeric, Boolean, Date
from app.database import Base

class Contratante(Base):
    __tablename__ = "contratante"

    CPF = Column(String(11), primary_key=True, unique=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String)
    telefone_emergencia = Column(String)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    endereco = Column(String)
    genero = Column(String) 
    data_nascimento = Column(Date)
