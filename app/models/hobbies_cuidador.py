from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class HobbiesCuidador(Base):
    __tablename__ = "hobbies_cuidador"
    
    id_hobbies_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    atividades_gosta = Column(String, nullable=False)
    atividades_manuais = Column(String(3), nullable=False)
    gerenero_musical = Column(String, nullable=False)
    filmes_tv = Column(String, nullable=False)
    participa_eventos = Column(String(3), nullable=False)
    gosta_ensinar = Column(String(3), nullable=False)
    atividades_tecnologicas = Column(String(3), nullable=False)
    comentarios = Column(String, nullable=False)
    
    id_cuidador = Column(Integer, ForeignKey('cuidador.id_cuidador'), nullable=False)
    cuidador = relationship("Cuidador", back_populates="hobbies")

    
