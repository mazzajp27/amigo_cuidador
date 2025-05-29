from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.crud import hobbies as crud_hobbies
from app.schemas.hobbies import HobbiesCreate, HobbiesUpdate, HobbiesResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/hobbies/{id_hobbies}", response_model=HobbiesResponse)
def read_hobbies(id_hobbies: int, db: Session = Depends(get_db)):
    db_hobbies = crud_hobbies.get_hobbie(db, id_hobbies)
    if db_hobbies is None:
        raise HTTPException(status_code=404, detail="Hobby não encontrado")
    return db_hobbies

@router.get("/hobbies", response_model=List[HobbiesResponse])
def read_hobbies(db: Session = Depends(get_db)):
    return crud_hobbies.get_hobbies(db)

@router.get("/hobbies/{id_contratante}", response_model=List[HobbiesResponse])
def read_hobbies(id_contratante: int, db: Session = Depends(get_db)):
    return crud_hobbies.get_hobbies_pelo_contratante(db, id_contratante)


@router.post("/hobbies/", response_model=HobbiesResponse)
def create_hobbie(hobbie: HobbiesCreate, db: Session = Depends(get_db)):
    return crud_hobbies.create_hobbie(db, hobbie)


@router.put("/hobbies/{id_hobbies}", response_model=HobbiesResponse)
def update_hobbie(id_hobbies: int, hobbie: HobbiesUpdate, db: Session = Depends(get_db)):
    db_hobbie = crud_hobbies.update_hobbie(db, id_hobbies, hobbie)
    if db_hobbie is None:
        raise HTTPException(status_code=404, detail="Hobby não encontrado")
    return db_hobbie

@router.delete("/hobbies/{id_hobbies}", response_model=HobbiesResponse)
def delete_hobbie(id_hobbies: int, db: Session = Depends(get_db)):
    db_hobbie = crud_hobbies.delete_hobbie(db, id_hobbies)
    if db_hobbie is None:
        raise HTTPException(status_code=404, detail="Hobby não encontrado")
    return db_hobbie 
    
