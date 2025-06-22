from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import contratante as crud_contratante
from app.crud import cuidador as crud_cuidador
from app.schemas.contratante import ContratanteResponse
from app.schemas.cuidador import CuidadorResponse
from pydantic import BaseModel
from typing import Union

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    senha: str

class LoginResponse(BaseModel):
    id: int
    nome: str
    email: str
    tipo_usuario: str  # "contratante" ou "cuidador"
    token: str = "dummy_token"  # Em uma aplicação real, você geraria um JWT real

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/login", response_model=LoginResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    # Primeiro, tenta encontrar como contratante
    contratante = db.query(crud_contratante.Contratante).filter(
        crud_contratante.Contratante.email == login_data.email
    ).first()
    
    if contratante and contratante.senha == login_data.senha:
        return LoginResponse(
            id=contratante.id_contratante,
            nome=contratante.nome,
            email=contratante.email,
            tipo_usuario="contratante"
        )
    
    # Se não encontrou como contratante, tenta como cuidador
    cuidador = db.query(crud_cuidador.Cuidador).filter(
        crud_cuidador.Cuidador.email == login_data.email
    ).first()
    
    if cuidador and cuidador.senha == login_data.senha:
        return LoginResponse(
            id=cuidador.id_cuidador,
            nome=cuidador.nome,
            email=cuidador.email,
            tipo_usuario="cuidador"
        )
    
    # Se não encontrou em nenhuma das tabelas
    raise HTTPException(status_code=401, detail="E-mail ou senha incorretos") 