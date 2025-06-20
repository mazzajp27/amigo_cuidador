from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HobbiesCuidadorBase(BaseModel):
    atividades_gosta: str
    pratica_esporte: str
    esporte_praticado: Optional[str] = None
    atividades_manuais: str
    atividades_manuais_praticadas: Optional[str] = None
    interesse_aprender: str
    interesse_aprender_especifico: Optional[str] = None
    gerenero_musical: str
    filmes_tv: str
    participa_eventos: str
    eventos: Optional[str] = None
    ensina: str
    ensinamentos_passados:Optional[str] = None
    atividades_tecnologicas: str
    atividades_tecnologicas_praticadas: Optional[str] = None
    outros_hobbies: Optional[str] = None
    id_cuidador: int
    
class HobbiesCuidadorCreate(HobbiesCuidadorBase):
    pass

class HobbiesCuidadorUpdate(HobbiesCuidadorBase):
    atividades_gosta: Optional[str] = None
    pratica_esporte: Optional[str] = None
    esporte_praticado: Optional[str] = None
    atividades_manuais: Optional[str] = None
    atividades_manuais_praticadas: Optional[str] = None
    interesse_aprender: Optional[str] = None
    interesse_aprender_especifico: Optional[str] = None
    gerenero_musical: Optional[str] = None
    filmes_tv: Optional[str] = None
    participa_eventos: Optional[str] = None
    eventos: Optional[str] = None
    ensina: Optional[str] = None
    ensinamentos_passados: Optional[str] = None
    atividades_tecnologicas: Optional[str] = None
    atividades_tecnologicas_praticadas: Optional[str] = None
    outros_hobbies: Optional[str] = None
    

class HobbiesCuidadorResponse(HobbiesCuidadorBase):
    id_hobbie: int
    
    class Config:
        from_attributes = True
