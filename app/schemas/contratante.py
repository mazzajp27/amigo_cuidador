from typing import Optional
from app.schemas.usuario import UsuarioBase
from pydantic import EmailStr
from datetime import date
from pydantic import BaseModel
from app.models.usuario import TipoUsuario

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

class ContratanteResponse(BaseModel):
    id_contratante: int
    usuario: Optional[dict] = None  # Dados do usuário relacionado

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
        # Criar um dicionário com os dados do objeto
        dict_data = {
            "id_contratante": obj.id_contratante,
            # Pegar os dados do usuário relacionado
            "nome": obj.usuario.nome,
            "cpf": obj.usuario.cpf,
            "email": obj.usuario.email,
            "telefone": obj.usuario.telefone,
            "telefone_emergencia": obj.usuario.telefone_emergencia,
            "senha": obj.usuario.senha,
            "genero": obj.usuario.genero,
            "data_nascimento": obj.usuario.data_nascimento,
            "tipo_usuario": obj.usuario.tipo_usuario,
        }
        return cls(**dict_data)
