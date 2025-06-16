from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.crud import questionario_cuidador as crud_questionario
from app.schemas.questionario_cuidador import QuestionarioCuidadorCreate, QuestionarioCuidadorUpdate, QuestionarioCuidadorResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/questionario-cuidador/{id_questionario_cuidador}", response_model=QuestionarioCuidadorResponse)
def read_questionario(id_questionario_cuidador: int, db: Session = Depends(get_db)):
    db_questionario = crud_questionario.get_questionario_cuidador(db, id_questionario_cuidador)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario

@router.get("/questionarios-cuidador", response_model=List[QuestionarioCuidadorResponse])
def read_questionarios(db: Session = Depends(get_db)):
    return crud_questionario.get_questionarios_cuidador(db)

@router.get("/questionarios-cuidador/{id_cuidador}", response_model=List[QuestionarioCuidadorResponse])
def read_questionarios_pelo_cuidador(id_cuidador: int, db: Session = Depends(get_db)):
    return crud_questionario.get_questionario_pelo_cuidador(db, id_cuidador)

@router.post("/questionario-cuidador/", response_model=QuestionarioCuidadorResponse)
def create_questionario(questionario: QuestionarioCuidadorCreate, db: Session = Depends(get_db)):
    return crud_questionario.create_questionario_cuidador(db, questionario)

@router.put("/questionario-cuidador/{id_questionario_cuidador}", response_model=QuestionarioCuidadorResponse)
def update_questionario(id_questionario_cuidador: int, questionario: QuestionarioCuidadorUpdate, db: Session = Depends(get_db)):
    db_questionario = crud_questionario.update_questionario_cuidador(db, id_questionario_cuidador, questionario)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario

@router.delete("/questionario-cuidador/{id_questionario_cuidador}", response_model=QuestionarioCuidadorResponse)
def delete_questionario(id_questionario_cuidador: int, db: Session = Depends(get_db)):
    db_questionario = crud_questionario.delete_questionario_cuidador(db, id_questionario_cuidador)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario 