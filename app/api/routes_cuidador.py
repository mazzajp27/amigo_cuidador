from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import cuidador as crud_cuidador
from app.crud import usuario as crud_usuario
from app.crud import endereco as crud_endereco
from app.schemas.cuidador import CuidadorCreate, CuidadorUpdate, CuidadorResponse
from app.schemas.usuario import UsuarioCreate
from app.schemas.endereco import EnderecoCreate
from app.models.usuario import TipoUsuario

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/cuidador/", response_model=CuidadorResponse)
def create_cuidador(cuidador: CuidadorCreate, db: Session = Depends(get_db)):
    # Check if email already exists
    db_usuario = crud_usuario.get_usuario_by_email(db, email=cuidador.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # Check if CPF already exists
    db_usuario = crud_usuario.get_usuario_by_cpf(db, cpf=cuidador.cpf)
    if db_usuario:
        raise HTTPException(status_code=400, detail="CPF já registrado")
    
    # Primeiro criamos o usuário
    usuario = UsuarioCreate(
        nome=cuidador.nome,
        cpf=cuidador.cpf,
        email=cuidador.email,
        telefone=cuidador.telefone,
        telefone_emergencia=cuidador.telefone_emergencia,
        senha=cuidador.senha,
        genero=cuidador.genero,
        data_nascimento=cuidador.data_nascimento,
        tipo_usuario=TipoUsuario.CUIDADOR
    )
    
    # Cria o usuário
    db_usuario = crud_usuario.create_usuario(db, usuario)
    
    # Cria o cuidador vinculado ao usuário
    return crud_cuidador.create_cuidador(db, cuidador, usuario_id=db_usuario.id_usuario)

@router.get("/cuidadores/", response_model=list[CuidadorResponse])
def read_cuidadores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cuidadores = crud_cuidador.get_cuidadores(db)
    return cuidadores[skip : skip + limit]

@router.get("/cuidador/{id_cuidador}", response_model=CuidadorResponse)
def read_cuidador(id_cuidador: int, db: Session = Depends(get_db)):
    db_cuidador = crud_cuidador.get_cuidador(db, id_cuidador)
    if db_cuidador is None:
        raise HTTPException(status_code=404, detail="Cuidador não encontrado")
    return db_cuidador

@router.put("/cuidador/{id_cuidador}", response_model=CuidadorResponse)
def update_cuidador(id_cuidador: int, cuidador: CuidadorUpdate, db: Session = Depends(get_db)):
    db_cuidador = crud_cuidador.update_cuidador(db, id_cuidador, cuidador)
    if db_cuidador is None:
        raise HTTPException(status_code=404, detail="Cuidador não encontrado")
    return db_cuidador

@router.delete("/cuidador/{id_cuidador}", response_model=CuidadorResponse)
def delete_cuidador(id_cuidador: int, db: Session = Depends(get_db)):
    db_cuidador = crud_cuidador.delete_cuidador(db, id_cuidador)
    if db_cuidador is None:
        raise HTTPException(status_code=404, detail="Cuidador não encontrado")
    return db_cuidador

@router.post("/cadastro/cuidador_completo/")
def cadastro_cuidador_completo(
    usuario: UsuarioCreate,
    cuidador: CuidadorCreate,
    endereco: EnderecoCreate,
    db: Session = Depends(get_db)
):
    # Check if email already exists
    db_usuario = crud_usuario.get_usuario_by_email(db, email=usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # Check if CPF already exists
    db_usuario = crud_usuario.get_usuario_by_cpf(db, cpf=usuario.cpf)
    if db_usuario:
        raise HTTPException(status_code=400, detail="CPF já registrado")
    
    # Cria usuário
    db_usuario = crud_usuario.create_usuario(db, usuario)
    # Cria cuidador vinculado ao usuário
    db_cuidador = crud_cuidador.create_cuidador(db, cuidador, usuario_id=db_usuario.id_usuario)
    # Cria endereço vinculado ao usuário
    db_endereco = crud_endereco.create_endereco(db, endereco, usuario_id=db_usuario.id_usuario)
    return {
        "usuario": db_usuario,
        "cuidador": db_cuidador,
        "endereco": db_endereco
    } 