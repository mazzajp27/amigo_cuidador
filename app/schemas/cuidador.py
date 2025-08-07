# app/schemas/cuidador.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from app.schemas.usuario import UsuarioBase

class CuidadorBase(UsuarioBase):
    pass

class CuidadorCreate(CuidadorBase):
    pass

class CuidadorUpdate(CuidadorBase):
    pass

class CuidadorResponse(CuidadorBase):
    id: int
    data_cadastro: date
    tipo: str
    status: str
    

    class Config:
        from_attributes = True  

class CuidadorListResponse(UsuarioBase):
    id: int
    data_cadastro: date
    tipo: str
    status: str

    class Config:
        from_attributes = True