from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Hobbies(Base):
    __tablename__ = "hobbies"
    
    id_hobbie = Column(Integer, primary_key=True, autoincrement=True)
    atividades_gosta = Column(String, nullable=False)
    pratica_esporte = Column(String(3), nullable=False)
    esporte_praticado = Column(String, nullable=False)
    atividades_manuais = Column(String(3), nullable=False)
    atividades_manuais_praticadas = Column(String, nullable=False)
    interesse_aprender = Column(String(3), nullable=False)
    interesse_aprender_especifico = Column(String, nullable=False)
    gerenero_musical = Column(String, nullable=False)
    filmes_tv = Column(String, nullable=False)
    participa_eventos = Column(String(3), nullable=False)
    eventos = Column(String, nullable=False)
    ensina = Column(String(3), nullable=False)
    ensinamentos_passados = Column(String, nullable=False)
    atividades_tecnologicas = Column(String(3), nullable=False)
    atividades_tecnologicas_praticadas = Column(String, nullable=False)
    outros_hobbies = Column(String, nullable=False)
    
    
    id_contratante = Column(Integer, ForeignKey('contratante.id_contratante'), nullable=False)
    contratante = relationship("Contratante", back_populates="hobbies")

    