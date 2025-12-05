from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class MensagemBase(BaseModel):
    texto: str

class MensagemCreate(MensagemBase):
    id_conversa: int
    id_remetente: int
    tipo_remetente: str  # 'contratante' ou 'cuidador'

class MensagemResponse(MensagemBase):
    id_mensagem: int
    id_conversa: int
    id_remetente: int
    tipo_remetente: str
    lida: bool
    created_at: datetime

    class Config:
        from_attributes = True

class ConversaBase(BaseModel):
    id_contratante: int
    id_cuidador: int

class ConversaCreate(ConversaBase):
    pass

class ConversaResponse(ConversaBase):
    id_conversa: int
    created_at: datetime
    mensagens: List[MensagemResponse] = []

    class Config:
        from_attributes = True

class ConversaComUltimaMensagem(BaseModel):
    id_conversa: int
    id_contratante: int
    id_cuidador: int
    nome_contratante: str
    nome_cuidador: str
    created_at: datetime
    ultima_mensagem: Optional[MensagemResponse] = None
    total_mensagens: int = 0
    mensagens_nao_lidas: int = 0

    class Config:
        from_attributes = True

