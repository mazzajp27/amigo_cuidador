from sqlalchemy import Column, Integer, String, Float, Numeric, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Cuidador(Base):
    __tablename__ = "cuidador"

    id_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(14), unique=True, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)
    telefone_emergencia = Column(String)
    senha = Column(String)
    genero = Column(String) 
    data_nascimento = Column(Date)
    
    # Relationships
    enderecos = relationship("EnderecoCuidador", back_populates="cuidador", cascade="all, delete-orphan")
    questionario = relationship("QuestionarioCuidador", back_populates="cuidador", cascade="all, delete-orphan")
    hobbies = relationship("HobbiesCuidador", back_populates="cuidador", cascade="all, delete-orphan")
