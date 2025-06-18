from pydantic import BaseModel
from typing import Optional

class EnderecoBase(BaseModel):
    estado: str
    cidade: str
    endereco: str
    bairro: str
    cep: str
    numero: str
    complemento: str
    referencia: Optional[str] = None
    usuario_id: int

class EnderecoCreate(EnderecoBase):
    pass

class EnderecoUpdate(BaseModel):
    cep: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    referencia: Optional[str] = None

class EnderecoResponse(EnderecoBase):
    id_endereco: int

    class Config:
        orm_mode = True 