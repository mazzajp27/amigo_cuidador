from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Cuidador(Base):
    __tablename__ = "cuidador"

    id_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id_usuario'), nullable=False, unique=True)
    usuario = relationship("Usuario", back_populates="cuidador")
    questionario = relationship("QuestionarioCuidador", back_populates="cuidador", cascade="all, delete-orphan")
  
   