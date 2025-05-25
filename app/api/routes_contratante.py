from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.crud import contratante as crud_contratante
from app.schemas.contratante import ContratanteCreate, ContratanteUpdate,  ContratanteResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/contratante/", response_model=ContratanteResponse)
def create_contratante(contratante: ContratanteCreate, db: Session = Depends(get_db)):
    return crud_contratante.create_contratante(db, contratante)

@router.get("/contratantes/", response_model=list[ContratanteResponse])
def read_contratantes(db: Session = Depends(get_db)):
    return crud_contratante.get_contratantes(db)

@router.get("/contratantes/{id_contratante}", response_model=ContratanteResponse)
def read_contratante(id_contratante: int, db: Session = Depends(get_db)):
    db_contratante = crud_contratante.get_contratante(db, id_contratante)
    if db_contratante is None:
        raise HTTPException(status_code=404, detail="Contratante não encontrado")
    return db_contratante

@router.put("/contratante/{id_contratante}", response_model=ContratanteResponse)
def update_contratante(id_contratante: int, contratante: ContratanteUpdate, db: Session = Depends(get_db)):
    db_contratante = crud_contratante.update_contratante(db, id_contratante, contratante)
    if db_contratante is None:
        raise HTTPException(status_code=404, detail="Contratante não encontrado")
    return db_contratante

@router.delete("/contratante/{id_contratante}", response_model=ContratanteResponse)
def delete_contratante(id_contratante:int, db: Session = Depends(get_db)):
    db_contratante = crud_contratante.delete_contratante(db, id_contratante)
    if db_contratante is None:
        raise HTTPException(status_code=404, detail="Contratante não encontrado")
    return db_contratante