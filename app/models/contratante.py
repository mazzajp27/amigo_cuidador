from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.usuario import Usuario


class Contratante(Usuario):
    __tablename__ = "contratante"

    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    
    # Relationship with Endereco
    enderecos = relationship("Endereco", back_populates="contratante", cascade="all, delete-orphan")
    questionario = relationship("Questionario", back_populates="contratante", cascade="all, delete-orphan")
    hobbies = relationship("Hobbies", back_populates="contratante", cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'contratante'
    }