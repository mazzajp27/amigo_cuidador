from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuestionarioBase(BaseModel):
    condicao_medica: str
    alergia: str
    restricao_alimentar: str
    restricao_mobilidade: str
    auxilio_atividades_diarias: str
    auxilio_medicacao: str
    monitoramento_sinais_vitais: str
    horario_preferencia: str
    frequencia_cuidado: str
    caracteristicas_cuidador: str
    observacoes: str
    id_contratante: int
class QuestionarioCreate(QuestionarioBase):
    pass

class QuestionarioUpdate(QuestionarioBase):
    condicao_medica: Optional[str] = None
    alergia: Optional[str] = None
    restricao_alimentar: Optional[str] = None
    restricao_mobilidade: Optional[str] = None
    auxilio_atividades_diarias: Optional[str] = None
    auxilio_medicacao: Optional[str] = None
    monitoramento_sinais_vitais: Optional[str] = None
    horario_preferencia: Optional[str] = None
    frequencia_cuidado: Optional[str] = None
    caracteristicas_cuidador: Optional[str] = None  
    observacoes: Optional[str] = None

    

class QuestionarioResponse(QuestionarioBase):
    id_questionario: int

    class Config:
        from_attributes = True