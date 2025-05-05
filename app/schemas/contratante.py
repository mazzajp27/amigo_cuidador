# app/schemas/shoes.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class ContratanteBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    email: Optional[str] = None
    senha: Optional[str] = None
    endereco: Optional[str] = None
    genero: Optional[str] = None 
    data_nascimento: Optional[date] = None

class ContratanteCreate(ContratanteBase):
    CPF: str

class ContratanteUpdate(ContratanteBase):
    pass

class ContratanteResponse(ContratanteBase):
    CPF: str

    class Config:
        orm_mode = True

