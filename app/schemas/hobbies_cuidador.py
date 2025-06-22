from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HobbiesCuidadorBase(BaseModel):
    atividades_gosta: str
    atividades_manuais: str
    gerenero_musical: str
    filmes_tv: str
    participa_eventos: str
    gosta_ensinar: str
    atividades_tecnologicas: str
    comentarios: str
    id_cuidador: int
    
class HobbiesCuidadorCreate(HobbiesCuidadorBase):
    pass

class HobbiesCuidadorUpdate(HobbiesCuidadorBase):
    atividades_gosta: Optional[str] = None
    atividades_manuais: Optional[str] = None
    gerenero_musical: Optional[str] = None
    filmes_tv: Optional[str] = None
    participa_eventos: Optional[str] = None
    gosta_ensinar: Optional[str] = None
    atividades_tecnologicas: Optional[str] = None
    comentarios: Optional[str] = None
    

class HobbiesCuidadorResponse(HobbiesCuidadorBase):
    id_hobbies_cuidador: int
    
    class Config:
        from_attributes = True
