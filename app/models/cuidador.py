from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.usuario import Usuario


class Cuidador(Usuario):
    __tablename__ = "cuidador"

    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    
    # Relationships
    enderecos = relationship("Endereco", back_populates="cuidador", cascade="all, delete-orphan")
    questionario = relationship("QuestionarioCuidador", back_populates="cuidador", cascade="all, delete-orphan")
    hobbies = relationship("HobbiesCuidador", back_populates="cuidador", cascade="all, delete-orphan")

    __mapper_args__ = {
        'polymorphic_identity': 'cuidador'
    }