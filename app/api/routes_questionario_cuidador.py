from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.crud import questionario_cuidador as crud_questionario_cuidador
from app.schemas.questionario_cuidador import QuestionarioCuidadorCreate, QuestionarioCuidadorUpdate, QuestionarioCuidadorResponse

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/questionario/{id_questionario_cuidador}", response_model=QuestionarioCuidadorResponse)
def read_questionario(id_questionario_cuidador: int, db: Session = Depends(get_db)):
    db_questionario = crud_questionario_cuidador.get_questionario(db, id_questionario_cuidador)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario

@router.get("/questionarios_cuidador", response_model=List[QuestionarioCuidadorResponse])
def read_questionarios(db: Session = Depends(get_db)):
    return crud_questionario_cuidador.get_questionarios(db)


@router.get("/questionarios_cuidador/{id_cuidador}", response_model=List[QuestionarioCuidadorResponse])
def read_questionarios(id_cuidador: int, db: Session = Depends(get_db)):
    return crud_questionario_cuidador.get_questionario_pelo_cuidador(db, id_cuidador) 


@router.post("/questionario_cuidador/", response_model=QuestionarioCuidadorResponse)
def create_questionario(questionario: QuestionarioCuidadorCreate, db: Session = Depends(get_db)):
    return crud_questionario_cuidador.create_questionario(db, questionario)

@router.put("/questionario_cuidador/{id_questionario_cuidador}", response_model=QuestionarioCuidadorResponse)
def update_questionario(id_questionario: int, questionario: QuestionarioCuidadorUpdate, db: Session = Depends(get_db)):
    db_questionario = crud_questionario_cuidador.update_questionario(db, id_questionario, questionario)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario

@router.delete("/questionario_cuidador/{id_questionario_cuidador}", response_model=QuestionarioCuidadorResponse)
def delete_questionario(id_questionario: int, db: Session = Depends(get_db)):
    db_questionario = crud_questionario_cuidador.delete_questionario(db, id_questionario)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario  