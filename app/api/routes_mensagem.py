from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import mensagem as crud_mensagem
from app.schemas.mensagem import MensagemCreate, MensagemResponse, ConversaResponse, ConversaComUltimaMensagem

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# IMPORTANTE: Rotas mais específicas devem vir ANTES das mais genéricas
@router.post("/conversas/", response_model=ConversaResponse)
def criar_ou_buscar_conversa(
    id_contratante: int = Query(..., description="ID do contratante"),
    id_cuidador: int = Query(..., description="ID do cuidador"),
    db: Session = Depends(get_db)
):
    """Cria uma nova conversa ou retorna a existente"""
    conversa = crud_mensagem.criar_ou_buscar_conversa(db, id_contratante, id_cuidador)
    return conversa

@router.get("/conversas/contratante/{id_contratante}", response_model=list[ConversaComUltimaMensagem])
def buscar_conversas_contratante(id_contratante: int, db: Session = Depends(get_db)):
    """Busca todas as conversas de um contratante"""
    conversas = crud_mensagem.buscar_conversas_por_contratante(db, id_contratante)
    return conversas

@router.get("/conversas/cuidador/{id_cuidador}", response_model=list[ConversaComUltimaMensagem])
def buscar_conversas_cuidador(id_cuidador: int, db: Session = Depends(get_db)):
    """Busca todas as conversas de um cuidador"""
    conversas = crud_mensagem.buscar_conversas_por_cuidador(db, id_cuidador)
    return conversas

@router.get("/conversas/{id_contratante}/{id_cuidador}", response_model=ConversaResponse)
def buscar_conversa_especifica(id_contratante: int, id_cuidador: int, db: Session = Depends(get_db)):
    """Busca uma conversa específica entre contratante e cuidador"""
    conversa = crud_mensagem.buscar_conversa_por_ids(db, id_contratante, id_cuidador)
    if not conversa:
        raise HTTPException(status_code=404, detail="Conversa não encontrada")
    return conversa

@router.post("/mensagens/", response_model=MensagemResponse)
def criar_mensagem(mensagem: MensagemCreate, db: Session = Depends(get_db)):
    """Cria uma nova mensagem"""
    return crud_mensagem.criar_mensagem(db, mensagem)

@router.get("/mensagens/conversa/{id_conversa}", response_model=list[MensagemResponse])
def buscar_mensagens_conversa(id_conversa: int, db: Session = Depends(get_db)):
    """Busca todas as mensagens de uma conversa"""
    mensagens = crud_mensagem.buscar_mensagens_por_conversa(db, id_conversa)
    return mensagens

@router.put("/mensagens/marcar-lidas/{id_conversa}")
def marcar_mensagens_lidas(id_conversa: int, tipo_usuario: str, db: Session = Depends(get_db)):
    """Marca mensagens como lidas"""
    if tipo_usuario not in ['contratante', 'cuidador']:
        raise HTTPException(status_code=400, detail="tipo_usuario deve ser 'contratante' ou 'cuidador'")
    crud_mensagem.marcar_mensagens_como_lidas(db, id_conversa, tipo_usuario)
    return {"message": "Mensagens marcadas como lidas"}

