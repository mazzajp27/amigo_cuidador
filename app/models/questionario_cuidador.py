from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class QuestionarioCuidador(Base):
    __tablename__ = "questionario_cuidador"

    id_questionario_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    cursos_realizados = Column(String)
    instituicao_ensino = Column(String)
    area_formacao = Column(String)
    tempo_experiencia = Column(String)
    responsabilidade_cuidado = Column(String)
    possui_certificacao = Column(String(3), nullable=False)
    certificacoes = Column(String)
    qualidades_preferencias = Column(String)
    horario_disponivel = Column(String)
    disponibilidade_plantao = Column(String(3), nullable=False)
    qualificacoes_cuidador = Column(String)
    referencia_cuidador = Column(String)


    
    

    # Foreign key relationship with Contratante
    id_cuidador = Column(Integer, ForeignKey('cuidador.id_cuidador'), nullable=False)
    cuidador = relationship("Cuidador", back_populates="questionario") 