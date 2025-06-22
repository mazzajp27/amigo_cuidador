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
def read_enderecos_by_cuidador(id_cuidador: int, db: Session = Depends(get_db)):
    return crud_endereco_cuidador.get_enderecos_pelo_cuidador(db, id_cuidador)


@router.post("/endereco_cuidador", response_model=EnderecoCuidadorResponse)
def create_endereco(endereco: EnderecoCuidadorCreate, db: Session = Depends(get_db)):
    db_endereco = crud_endereco_cuidador.create_endereco(db, endereco)
    return {
        "id_endereco_cuidador": db_endereco.id_endereco_cuidador,
        "estado": db_endereco.estado,
        "cidade": db_endereco.cidade,
        "endereco": db_endereco.endereco,
        "bairro": db_endereco.bairro,
        "cep": db_endereco.cep,
        "numero": db_endereco.numero,
        "complemento": db_endereco.complemento,
        "referencia": db_endereco.referencia,
        "id_cuidador": db_endereco.id_cuidador
    }


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