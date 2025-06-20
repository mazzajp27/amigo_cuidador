from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class QuestionarioCuidadorBase(BaseModel):
    cursos_realizados: str
    instituicao_ensino: str
    area_formacao: str
    tempo_experiencia: str
    principais_responsabilidades: str
    possui_certificacao: str
    certificacao: str
    qualidades_preferencias: str
    horario_disponivel: str
    disponibilidade_plantao: str
    qualidades_cuidador: str
    referencia_cuidador: str
    id_cuidador: int

class QuestionarioCuidadorCreate(QuestionarioCuidadorBase):
    pass

class QuestionarioCuidadorUpdate(QuestionarioCuidadorBase):
    cursos_realizados: Optional[str] = None
    instituicao_ensino: Optional[str] = None
    area_formacao: Optional[str] = None
    tempo_experiencia: Optional[str] = None
    principais_responsabilidades: Optional[str] = None
    possui_certificacao: Optional[str] = None
    certificacao: Optional[str] = None
    qualidades_preferencias: Optional[str] = None
    horario_disponivel: Optional[str] = None
    disponibilidade_plantao: Optional[str] = None
    qualidades_cuidador: Optional[str] = None
    referencia_cuidador: Optional[str] = None

class QuestionarioCuidadorResponse(QuestionarioCuidadorBase):
    id_questionario: int

    class Config:
        from_attributes = True
