from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuestionarioBase(BaseModel):
    possui_condicao_medica: str
    condicao_medica:  Optional[str] = None
    toma_medicamento: str
    medicamento:  Optional[str] = None
    realiza_atividades_diarias: str
    atividades_diarias_ajuda:  Optional[str] = None
    familia_apoio: str
    frequencia_visitas:  Optional[str] = None
    principais_qualidades_preferencias: str
    espera_cuidador: str
    possui_deficiencias: str
    deficiencias:  Optional[str] = None
    observacoes: Optional[str] = None
    id_contratante: int

class QuestionarioCreate(QuestionarioBase):
    pass

class QuestionarioUpdate(QuestionarioBase):
    possui_condicao_medica: Optional[str] = None
    condicao_medica: Optional[str] = None
    toma_medicamento: Optional[str] = None
    medicamento: Optional[str] = None
    realiza_atividades_diarias: Optional[str] = None
    atividades_diarias_ajuda: Optional[str] = None
    familia_apoio: Optional[str] = None
    frequencia_visitas: Optional[str] = None
    principais_qualidades_preferencias: Optional[str] = None
    espera_cuidador: Optional[str] = None
    possui_deficiencias: Optional[str] = None
    deficiencias: Optional[str] = None
    observacoes: Optional[str] = None
    

class QuestionarioResponse(QuestionarioBase):
    id_questionario: int

    class Config:
        from_attributes = True
