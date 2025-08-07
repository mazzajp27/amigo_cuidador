# app/schemas/contratante.py

from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from app.schemas.usuario import UsuarioBase

class ContratanteBase(UsuarioBase):
    pass

class ContratanteCreate(ContratanteBase):
    pass

class ContratanteUpdate(ContratanteBase):
   pass
        
class ContratanteResponse(ContratanteBase):
    id: int
    data_cadastro: date
    tipo: str
    status: str
    
    class Config:
        from_attributes = True

class ContratanteListResponse(UsuarioBase):
    id: int
    data_cadastro: date
    tipo: str
    status: str

    class Config:
        from_attributes = True