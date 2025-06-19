from sqlalchemy import Column, Integer, String, Float, Numeric, Boolean, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import enum

class TipoUsuario(enum.Enum):
    CONTRATANTE = "contratante"
    CUIDADOR = "cuidador"

class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    cpf = Column(String(14), unique=True, index=True)
    email = Column(String, unique=True, index=True)
    telefone = Column(String)
    telefone_emergencia = Column(String)
    senha = Column(String)
    genero = Column(String) 
    data_nascimento = Column(Date)
    tipo_usuario = Column(Enum(TipoUsuario), nullable=False)

    # Relationships
    contratante = relationship("Contratante", back_populates="usuario", uselist=False, cascade="all, delete-orphan")
    cuidador = relationship("Cuidador", back_populates="usuario", uselist=False, cascade="all, delete-orphan")
    enderecos = relationship("Endereco", back_populates="usuario", cascade="all, delete-orphan")
    hobbies = relationship("Hobbies", back_populates="usuario", cascade="all, delete-orphan")