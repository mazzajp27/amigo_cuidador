# app/schemas/shoes.py

from pydantic import BaseModel, EmailStr
from typing import Optional

class ContratanteBase(BaseModel):
    nome: str
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    email: Optional[EmailStr] = None
    senha: Optional[str] = None
    endereco: Optional[str] = None
    genero: Optional[str] = None 
    idade: Optional[int] = None

class ContratanteCreate(ContratanteBase):
    CPF: int

class ContratanteUpdate(ContratanteBase):
    pass

class ContratanteResponse(ContratanteBase):
    CPF: int

    class Config:
        orm_mode = True

