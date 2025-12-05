# app/schemas/cuidador.py

from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
from datetime import date

class CuidadorBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    senha: str
    genero: Optional[str] = None 
    data_nascimento: Optional[date] = None

class CuidadorCreate(CuidadorBase):
    # Campos opcionais para dados relacionados que vêm do frontend
    estado: Optional[str] = None
    cidade: Optional[str] = None
    endereco: Optional[str] = None
    bairro: Optional[str] = None
    cep: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    referencia: Optional[str] = None
    formacaoAcademica: Optional[Dict[str, Any]] = None
    experienciaProfissional: Optional[Dict[str, Any]] = None
    qualidades: Optional[Dict[str, Any]] = None
    referencias: Optional[Dict[str, Any]] = None
    interesses: Optional[Dict[str, Any]] = None

class CuidadorUpdate(CuidadorBase):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    senha: Optional[str] = None
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None

class CuidadorResponse(CuidadorBase):
    id_cuidador: int

    class Config:
        orm_mode = True

