from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.crud import hobbies_cuidador as crud_hobbies_cuidador
from app.schemas.hobbies_cuidador import HobbiesCuidadorCreate, HobbiesCuidadorUpdate, HobbiesCuidadorResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/hobbie/{id_hobbies_cuidador}", response_model=HobbiesCuidadorResponse)
def read_hobbies(id_hobbies_cuidador: int, db: Session = Depends(get_db)):
    db_hobbies = crud_hobbies_cuidador.get_hobbie(db, id_hobbies_cuidador)
    if db_hobbies is None:
        raise HTTPException(status_code=404, detail="Hobby não encontrado")
    return db_hobbies

@router.get("/hobbies_cuidador", response_model=List[HobbiesCuidadorResponse])
def read_hobbies(db: Session = Depends(get_db)):
    return crud_hobbies_cuidador.get_hobbies(db)


@router.get("/hobbies_cuidador/{id_cuidador}", response_model=List[HobbiesCuidadorResponse])
def read_hobbies(id_cuidador: int, db: Session = Depends(get_db)):
    return crud_hobbies_cuidador.get_hobbies_pelo_cuidador(db, id_cuidador)


@router.post("/hobbies_cuidador/", response_model=HobbiesCuidadorResponse)
def create_hobbie(hobbie: HobbiesCuidadorCreate, db: Session = Depends(get_db)):
    return crud_hobbies_cuidador.create_hobbie(db, hobbie)


@router.put("/hobbies_cuidador/{id_hobbies_cuidador}", response_model=HobbiesCuidadorResponse)
def update_hobbie(id_hobbies_cuidador: int, hobbie: HobbiesCuidadorUpdate, db: Session = Depends(get_db)):
    db_hobbie = crud_hobbies_cuidador.update_hobbie(db, id_hobbies_cuidador, hobbie)
    if db_hobbie is None:
        raise HTTPException(status_code=404, detail="Hobby não encontrado")
    return db_hobbie

@router.delete("/hobbies_cuidador/{id_hobbies_cuidador}", response_model=HobbiesCuidadorResponse)
def delete_hobbie(id_hobbies_cuidador: int, db: Session = Depends(get_db)):
    db_hobbie = crud_hobbies_cuidador.delete_hobbie(db, id_hobbies_cuidador)
    if db_hobbie is None:
        raise HTTPException(status_code=404, detail="Hobby não encontrado")
    return db_hobbie 
    
