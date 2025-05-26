from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.crud import questionario as crud_questionario
from app.schemas.questionario import Questionario, QuestionarioCreate

router = APIRouter()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[Questionario])
def read_questionarios(
    db: Session = Depends(get_db),
    skip: int = 0,
    limit: int = 100
):
    questionarios = crud_questionario.get_questionarios(db, skip=skip, limit=limit)
    return questionarios

@router.post("/", response_model=Questionario)
def create_questionario(
    *,
    db: Session = Depends(get_db),
    questionario_in: QuestionarioCreate
):
    questionario = crud_questionario.create_questionario(db=db, questionario=questionario_in)
    return questionario

@router.get("/{questionario_id}", response_model=Questionario)
def read_questionario(
    *,
    db: Session = Depends(get_db),
    questionario_id: int
):
    questionario = crud_questionario.get_questionario(db=db, questionario_id=questionario_id)
    if not questionario:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return questionario

@router.put("/{questionario_id}", response_model=Questionario)
def update_questionario(
    *,
    db: Session = Depends(get_db),
    questionario_id: int,
    questionario_in: QuestionarioCreate
):
    questionario = crud_questionario.update_questionario(
        db=db, questionario_id=questionario_id, questionario=questionario_in
    )
    if not questionario:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return questionario

@router.delete("/{questionario_id}")
def delete_questionario(
    *,
    db: Session = Depends(get_db),
    questionario_id: int
):
    success = crud_questionario.delete_questionario(db=db, questionario_id=questionario_id)
    if not success:
        raise HTTPException(status_code=404, detail="Questionário não encontrado")
    return {"message": "Questionário deletado com sucesso"} 