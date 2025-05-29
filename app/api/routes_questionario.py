from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.crud import questionario as crud_questionario
from app.schemas.questionario import QuestionarioCreate, QuestionarioUpdate, QuestionarioResponse

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/questionario/{id_questionario}", response_model=QuestionarioResponse)
def read_questionario(id_questionario: int, db: Session = Depends(get_db)):
    db_questionario = crud_questionario.get_questionario(db, id_questionario)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario

@router.get("/questionarios", response_model=List[QuestionarioResponse])
def read_questionarios(db: Session = Depends(get_db)):
    return crud_questionario.get_questionarios(db)


@router.get("/questionarios/{id_contratante}", response_model=List[QuestionarioResponse])
def read_questionarios(id_contratante: int, db: Session = Depends(get_db)):
    return crud_questionario.get_questionario_pelo_contratante(db, id_contratante) 


@router.post("/questionario/", response_model=QuestionarioResponse)
def create_questionario(questionario: QuestionarioCreate, db: Session = Depends(get_db)):
    return crud_questionario.create_questionario(db, questionario)

@router.put("/questionario/{id_questionario}", response_model=QuestionarioResponse)
def update_questionario(id_questionario: int, questionario: QuestionarioUpdate, db: Session = Depends(get_db)):
    db_questionario = crud_questionario.update_questionario(db, id_questionario, questionario)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario

@router.delete("/questionario/{id_questionario}", response_model=QuestionarioResponse)
def delete_questionario(id_questionario: int, db: Session = Depends(get_db)):
    db_questionario = crud_questionario.delete_questionario(db, id_questionario)
    if db_questionario is None:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return db_questionario  