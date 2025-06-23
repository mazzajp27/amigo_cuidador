# app/schemas/contratante.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ContratanteBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: Optional[str] = None 
    data_nascimento: Optional[date] = None

class ContratanteCreate(ContratanteBase):
    pass

class ContratanteUpdate(ContratanteBase):
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

    class Config:
        orm_mode = True