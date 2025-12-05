# app/schemas/contratante.py

from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, Any
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
    # Campos opcionais para dados relacionados que vêm do frontend
    estado: Optional[str] = None
    cidade: Optional[str] = None
    endereco: Optional[str] = None
    bairro: Optional[str] = None
    cep: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    referencia: Optional[str] = None
    questionario: Optional[Dict[str, Any]] = None
    hobbies: Optional[list] = None
    atividadesFisicas: Optional[Dict[str, Any]] = None
    atividadesSociais: Optional[Dict[str, Any]] = None
    preferencias: Optional[Dict[str, Any]] = None

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

