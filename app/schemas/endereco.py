from pydantic import BaseModel
from typing import Optional

class EnderecoBase(BaseModel):
    estado: str
    cidade: str
    endereco: str
    bairro: str
    cep: str
    numero: str
    complemento: Optional[str] = None
    referencia: Optional[str] = None


class EnderecoCreate(EnderecoBase):
    id_contratante: Optional[int] = None
    id_cuidador: Optional[int] = None

class EnderecoUpdate(BaseModel):
    cep: Optional[str] = None
    endereco: Optional[str] = None
    numero: Optional[str] = None
    complemento: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    referencia: Optional[str] = None
    id_contratante: Optional[int] = None
    id_cuidador: Optional[int] = None

class EnderecoResponse(EnderecoBase):
    id_endereco: int
    id_contratante: Optional[int] = None
    id_cuidador: Optional[int] = None

    class Config:
        from_attributes = True 