from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import endereco as crud_endereco
from app.schemas.endereco import EnderecoCreate, EnderecoUpdate, EnderecoResponse
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/endereco/", response_model=EnderecoResponse)
def create_endereco(endereco: EnderecoCreate, db: Session = Depends(get_db)):
    return crud_endereco.create_endereco(db, endereco)

@router.get("/enderecos/{id_contratante}", response_model=List[EnderecoResponse])
def read_enderecos(id_contratante: int, db: Session = Depends(get_db)):
    return crud_endereco.get_enderecos(db, id_contratante)

@router.get("/endereco/{id_endereco}", response_model=EnderecoResponse)
def read_endereco(id_endereco: int, db: Session = Depends(get_db)):
    db_endereco = crud_endereco.get_endereco(db, id_endereco)
    if db_endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco

@router.put("/endereco/{id_endereco}", response_model=EnderecoResponse)
def update_endereco(id_endereco: int, endereco: EnderecoUpdate, db: Session = Depends(get_db)):
    db_endereco = crud_endereco.update_endereco(db, id_endereco, endereco)
    if db_endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco

@router.delete("/endereco/{id_endereco}", response_model=EnderecoResponse)
def delete_endereco(id_endereco: int, db: Session = Depends(get_db)):
    db_endereco = crud_endereco.delete_endereco(db, id_endereco)
    if db_endereco is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")
    return db_endereco 