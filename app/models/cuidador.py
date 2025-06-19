from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Cuidador(Base):
    __tablename__ = "cuidador"

    id_cuidador = Column(Integer, ForeignKey('usuario.id_usuario', ondelete='CASCADE'), primary_key=True)
    usuario = relationship("Usuario", back_populates="cuidador", lazy='joined', innerjoin=True)
    questionario = relationship("QuestionarioCuidador", back_populates="cuidador", cascade="all, delete-orphan")