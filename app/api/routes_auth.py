from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import contratante as crud_contratante
from app.schemas.contratante import ContratanteResponse
from pydantic import BaseModel
from app.crud import usuario as crud_usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    senha: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/login", response_model=ContratanteResponse)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    # Find user by email
    user = db.query(crud_contratante.Contratante).filter(
        crud_contratante.Contratante.email == login_data.email
    ).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    # Verify password (in a real application, you should use proper password hashing)
    if user.senha != login_data.senha:
        raise HTTPException(status_code=401, detail="Senha incorreta")
    
    return user 

@router.post("/usuario/", response_model=UsuarioResponse)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica se já existe usuário com o mesmo email ou CPF
    if crud_usuario.get_usuario_by_email(db, usuario.email):
        raise HTTPException(status_code=400, detail="Email já registrado")
    if crud_usuario.get_usuario_by_cpf(db, usuario.cpf):
        raise HTTPException(status_code=400, detail="CPF já registrado")
    return crud_usuario.create_usuario(db, usuario) 