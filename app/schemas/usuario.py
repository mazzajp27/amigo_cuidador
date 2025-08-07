from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date


class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: str
    data_nascimento: date
    

class UsuarioCreate(UsuarioBase):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None
    tipo: str

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    senha: Optional[str] = None
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None
    tipo: Optional[str] = None

class UsuarioResponse(UsuarioBase):
    id: int
    data_cadastro: date
    tipo: str
    status: str

    class Config:
        from_attributes = True
