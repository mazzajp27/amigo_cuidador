from pydantic import BaseModel
from typing import Optional

class EnderecoCuidadorBase(BaseModel):
    estado: str
    cidade: str
    endereco: str
    bairro: str
    cep: str
    numero: str
    complemento: str
    referencia: Optional[str] = None
    id_cuidador: int


class EnderecoCuidadorCreate(EnderecoCuidadorBase):
    pass

class EnderecoCuidadorUpdate(BaseModel):
    cep: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    referencia: Optional[str] = None

class EnderecoCuidadorResponse(EnderecoCuidadorBase):
    id_endereco: int

    class Config:
        orm_mode = True 