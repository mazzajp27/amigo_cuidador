from pydantic import BaseModel
from typing import Optional

class QuestionarioCuidadorBase(BaseModel):
    cursos_realizados: Optional[str] = None
    instituicao_ensino: Optional[str] = None
    area_formacao: Optional[str] = None
    tempo_experiencia: Optional[str] = None
    responsabilidade_cuidado: Optional[str] = None
    possui_certificacao: str
    certificacoes: Optional[str] = None
    qualidades_preferencias: Optional[str] = None
    horario_disponivel: Optional[str] = None
    disponibilidade_plantao: str
    qualificacoes_cuidador: Optional[str] = None
    referencia_cuidador: Optional[str] = None
    id_cuidador: int

class QuestionarioCuidadorCreate(QuestionarioCuidadorBase):
    pass

class QuestionarioCuidadorUpdate(QuestionarioCuidadorBase):
    cursos_realizados: Optional[str] = None
    instituicao_ensino: Optional[str] = None
    area_formacao: Optional[str] = None
    tempo_experiencia: Optional[str] = None
    responsabilidade_cuidado: Optional[str] = None
    possui_certificacao: Optional[str] = None
    certificacoes: Optional[str] = None
    qualidades_preferencias: Optional[str] = None
    horario_disponivel: Optional[str] = None
    disponibilidade_plantao: Optional[str] = None
    qualificacoes_cuidador: Optional[str] = None
    referencia_cuidador: Optional[str] = None
    id_cuidador: Optional[int] = None

class QuestionarioCuidadorResponse(QuestionarioCuidadorBase):
    id_questionario_cuidador: int

    class Config:
        orm_mode = True 