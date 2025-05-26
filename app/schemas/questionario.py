from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuestionarioBase(BaseModel):
    possui_condicao_medica: str
    condicao_medica: str
    toma_medicamento: str
    medicamento: str
    realiza_atividades_diarias: str
    atividades_diarias: str
    familia_apoio: str
    frequencia_visitas: str
    principais_qualidades_preferencias: Optional[str] = None
    espera_cuidador: str
    possui_deficiencias: str
    deficiencias: str
    observacoes: Optional[str] = None
    id_contratante: int

class QuestionarioCreate(QuestionarioBase):
    pass

class Questionario(QuestionarioBase):
    id_questionario: int

    class Config:
        from_attributes = True
