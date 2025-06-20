from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import endereco_cuidador as crud_endereco_cuidador
from app.schemas.endereco_cuidador import EnderecoCuidadorCreate, EnderecoCuidadorUpdate, EnderecoCuidadorResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/endereco_cuidador/{id_endereco_cuidador}", response_model=EnderecoCuidadorResponse)
def read_endereco(id_endereco_cuidador: int, db: Session = Depends(get_db)):
    db_endereco = crud_endereco_cuidador.get_endereco(db, id_endereco_cuidador)
    if db_endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco


@router.get("/enderecos_cuidador", response_model=List[EnderecoCuidadorResponse])
def read_enderecos(db: Session = Depends(get_db)):
    return crud_endereco_cuidador.get_enderecos(db)


@router.get("/enderecos_cuidador/{id_cuidador}", response_model=List[EnderecoCuidadorResponse])
def read_enderecos(id_cuidador: int, db: Session = Depends(get_db)):
    return crud_endereco_cuidador.get_enderecos_pelo_cuidador(db, id_cuidador)


@router.post("/endereco_cuidador/", response_model=EnderecoCuidadorResponse)
def create_endereco(endereco: EnderecoCuidadorCreate, db: Session = Depends(get_db)):
    return crud_endereco_cuidador.create_endereco(db, endereco)


@router.put("/endereco_cuidador/{id_endereco_cuidador}", response_model=EnderecoCuidadorResponse)
def update_endereco(id_endereco_cuidador: int, endereco: EnderecoCuidadorUpdate, db: Session = Depends(get_db)):
    db_endereco = crud_endereco_cuidador.update_endereco(db, id_endereco_cuidador, endereco)
    if db_endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco


@router.delete("/endereco_cuidador/{id_endereco_cuidador}", response_model=EnderecoCuidadorResponse)
def delete_endereco(id_endereco_cuidador: int, db: Session = Depends(get_db)):
    db_endereco = crud_endereco_cuidador.delete_endereco(db, id_endereco_cuidador)
    if db_endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco 