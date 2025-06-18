from typing import Optional
from app.schemas.usuario import UsuarioBase
from pydantic import EmailStr
from datetime import date
from pydantic import BaseModel

class ContratanteBase(UsuarioBase):
    pass

class ContratanteCreate(ContratanteBase):
    pass

class ContratanteUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    senha: Optional[str] = None
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None

class ContratanteResponse(ContratanteBase):
    id_contratante: int
    usuario_id: int

    class Config:
        orm_mode = True
