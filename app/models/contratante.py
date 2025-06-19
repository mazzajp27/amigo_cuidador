from sqlalchemy import Column, Integer, String, Float, Numeric, Boolean, Date
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import ForeignKey

class Contratante(Base):
    __tablename__ = "contratante"

    id_contratante = Column(Integer, ForeignKey('usuario.id_usuario'), primary_key=True)
    usuario = relationship("Usuario", back_populates="contratante")
    questionario = relationship("QuestionarioContratante", back_populates="contratante", cascade="all, delete-orphan")
    
