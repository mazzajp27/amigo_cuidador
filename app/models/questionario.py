from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Questionario(Base):
    __tablename__ = "questionario"

    id_questionario = Column(Integer, primary_key=True, autoincrement=True)
    condicao_medica = Column(String, nullable=True)
    medicamento = Column(String, nullable=True)
    alergia = Column(String, nullable=True)
    restricao_alimentar = Column(String, nullable=True)
    restricao_mobilidade = Column(String, nullable=True)
    auxilio_atividades_diarias = Column(String(3), nullable=False)
    auxilio_medicacao = Column(String(3), nullable=False)
    monitoramento_sinais_vitais = Column(String(3), nullable=False)
    horario_preferencia = Column(String, nullable=True)
    frequencia_cuidado = Column(String, nullable=True)
    caracteristicas_cuidador = Column(String, nullable=True)
    observacoes = Column(String, nullable=True)
    

    # Foreign key relationship with Contratante
    id_contratante = Column(Integer, ForeignKey('contratante.id_contratante'), nullable=False)
    contratante = relationship("Contratante", back_populates="questionario") 
    