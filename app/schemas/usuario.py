from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from app.models.usuario import TipoUsuario

class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None
    tipo_usuario: TipoUsuario

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    senha: Optional[str] = None
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None

class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        orm_mode = True
