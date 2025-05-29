from sqlalchemy.orm import Session
from app.models.questionario import Questionario
from app.schemas.questionario import QuestionarioCreate, QuestionarioUpdate

def get_questionario(db: Session, id_questionario: int):
    return db.query(Questionario).filter(Questionario.id_questionario == id_questionario).first()


def get_questionarios(db: Session):
    return db.query(Questionario).all()


def get_questionario_pelo_contratante(db: Session, id_contratante: int):
    return db.query(Questionario).filter(Questionario.id_contratante == id_contratante).all()


def create_questionario(db: Session, questionario: QuestionarioCreate):
    db_questionario = Questionario(**questionario.dict())
    db.add(db_questionario)
    db.commit()
    db.refresh(db_questionario)
    return db_questionario


def update_questionario(db: Session, id_questionario: int, questionario: QuestionarioUpdate):
    db_questionario = db.query(Questionario).filter(Questionario.id_questionario == id_questionario).first()
    if db_questionario:
        for key, value in questionario.dict(exclude_unset=True).items():
            setattr(db_questionario, key, value)
        db.commit()
        db.refresh(db_questionario)
    return db_questionario

def delete_questionario(db: Session, id_questionario: int):
    db_questionario = db.query(Questionario).filter(Questionario.id_questionario == id_questionario).first()
    if db_questionario is None:
        return None
    db.delete(db_questionario)
    db.commit()
    return db_questionario 
