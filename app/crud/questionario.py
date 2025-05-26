from sqlalchemy.orm import Session
from app.models.questionario import Questionario
from app.schemas.questionario import QuestionarioCreate, Questionario as QuestionarioSchema

def get_questionario(db: Session, questionario_id: int):
    return db.query(Questionario).filter(Questionario.id_questionario == questionario_id).first()

def get_questionario_by_contratante(db: Session, contratante_id: int):
    return db.query(Questionario).filter(Questionario.id_contratante == contratante_id).first()

def get_questionarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Questionario).offset(skip).limit(limit).all()

def create_questionario(db: Session, questionario: QuestionarioCreate):
    db_questionario = Questionario(**questionario.dict())
    db.add(db_questionario)
    db.commit()
    db.refresh(db_questionario)
    return db_questionario

def update_questionario(db: Session, questionario_id: int, questionario: QuestionarioCreate):
    db_questionario = get_questionario(db, questionario_id)
    if db_questionario:
        for key, value in questionario.dict().items():
            setattr(db_questionario, key, value)
        db.commit()
        db.refresh(db_questionario)
    return db_questionario

def delete_questionario(db: Session, questionario_id: int):
    db_questionario = get_questionario(db, questionario_id)
    if db_questionario:
        db.delete(db_questionario)
        db.commit()
        return True
    return False
