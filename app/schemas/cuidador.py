from typing import Optional
from pydantic import EmailStr, BaseModel
from datetime import date
from app.models.usuario import TipoUsuario

class CuidadorBase(BaseModel):
    pass

class CuidadorCreate(BaseModel):
    nome: str
    cpf: str
    email: EmailStr
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None

class CuidadorUpdate(BaseModel):
    nome: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    telefone_emergencia: Optional[str] = None
    senha: Optional[str] = None
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None

class CuidadorResponse(BaseModel):
    id_cuidador: int

    # Campos do usuário
    nome: str
    cpf: str
    email: str
    telefone: str
    telefone_emergencia: Optional[str] = None
    senha: str
    genero: Optional[str] = None
    data_nascimento: Optional[date] = None
    tipo_usuario: TipoUsuario

    class Config:
        orm_mode = True

    @classmethod
    def from_orm(cls, obj):
        if not hasattr(obj, 'usuario') or obj.usuario is None:
            raise ValueError("Objeto Cuidador deve ter um usuário associado")
            
        return cls(
            id_cuidador=obj.id_cuidador,
            nome=obj.usuario.nome,
            cpf=obj.usuario.cpf,
            email=obj.usuario.email,
            telefone=obj.usuario.telefone,
            telefone_emergencia=obj.usuario.telefone_emergencia,
            senha=obj.usuario.senha,
            genero=obj.usuario.genero,
            data_nascimento=obj.usuario.data_nascimento,
            tipo_usuario=obj.usuario.tipo_usuario
        )