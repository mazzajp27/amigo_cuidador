from sqlalchemy import Column, Integer, String, Float, Numeric, Boolean, Date
from app.database import Base

class Contratante(Base):
    __tablename__ = "contratante"


    id_contratante = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(14), unique=True, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)
    telefone_emergencia = Column(String)
    senha = Column(String)
    genero = Column(String) 
    data_nascimento = Column(Date)
