from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class QuestionarioCuidador(Base):
    __tablename__ = "questionario_cuidador"

    id_questionario_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    cursos_realizados = Column(String, nullable=False)
    instituicao_ensino = Column(String, nullable=False)
    area_formacao = Column(String, nullable=False)
    tempo_experiencia = Column(String, nullable=False)
    principais_responsabilidades = Column(String, nullable=False)
    possui_certificacao = Column(String(3), nullable=False)
    certificacao = Column(String, nullable=False)
    qualidades_preferencias = Column(String, nullable=False)
    horario_disponivel = Column(String, nullable=False)
    disponibilidade_plantao = Column(String, nullable=False)
    qualidades_cuidador = Column(String, nullable=False)
    referencia_cuidador = Column(String, nullable=False)
    
    

    # Foreign key relationship with Contratante
    id_cuidador = Column(Integer, ForeignKey('cuidador.id_cuidador'), nullable=False)
    cuidador = relationship("Cuidador", back_populates="questionario") 
    