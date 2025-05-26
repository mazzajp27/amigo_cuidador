from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Questionario(Base):
    __tablename__ = "questionario"

    id_questionario = Column(Integer, primary_key=True, autoincrement=True)
    possui_condicao_medica = Column(String(3), nullable=False)
    condicao_medica = Column(String, nullable=False)
    toma_medicamento = Column(String(3), nullable=False)
    medicamento = Column(String, nullable=False)
    realiza_atividades_diarias = Column(String(3), nullable=False)
    atividades_diarias_ajuda = Column(String, nullable=False)
    familia_apoio = Column(String(3), nullable=False)
    frequencia_visitas = Column(String, nullable=False)
    principais_qualidades_preferencias = Column(String)
    espera_cuidador = Column(String, nullable=False)
    possui_deficiencias = Column(String(3), nullable=False)
    deficiencias = Column(String, nullable=False)
    observacoes = Column(String)
    

    # Foreign key relationship with Contratante
    id_contratante = Column(Integer, ForeignKey('contratante.id_contratante'), nullable=False)
    contratante = relationship("Contratante", back_populates="questionario") 
    