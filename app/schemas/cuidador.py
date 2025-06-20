# app/schemas/contratante.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class CuidadorBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: Optional[str] = None 
    data_nascimento: Optional[date] = None

class CuidadorCreate(CuidadorBase):
    pass

class CuidadorUpdate(CuidadorBase):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    senha: Optional[str] = None
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None

class CuidadorResponse(CuidadorBase):
    id_cuidador: int

    class Config:
        orm_mode = True

