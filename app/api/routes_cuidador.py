from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import cuidador as crud_cuidador
from app.schemas.cuidador import CuidadorCreate, CuidadorUpdate, CuidadorResponse

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
    db_cuidador = crud_cuidador.get_cuidador_by_email(db, email=cuidador.email)
    if db_cuidador:
        raise HTTPException(status_code=400, detail="Email já registrado")
    
    # Check if CPF already exists
    db_cuidador = crud_cuidador.get_cuidador_by_cpf(db, cpf=cuidador.cpf)
    if db_cuidador:
        raise HTTPException(status_code=400, detail="CPF já registrado")
    
    return crud_cuidador.create_cuidador(db, cuidador)

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