
from sqlalchemy.orm import Session
from app.models.questionario_cuidador import QuestionarioCuidador
from app.schemas.questionario_cuidador import QuestionarioCuidadorCreate, QuestionarioCuidadorUpdate

def get_questionario(db: Session, id_questionario: int):
    return db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_questionario == id_questionario).first()


def get_questionarios(db: Session):
    return db.query(QuestionarioCuidador).all()


def get_questionario_pelo_cuidador(db: Session, id_cuidador: int):
    return db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_cuidador == id_cuidador).all()


def create_questionario(db: Session, questionario: QuestionarioCuidadorCreate):
    db_questionario_cuidador = QuestionarioCuidador(**questionario.dict())
    db.add(db_questionario_cuidador)
    db.commit()
    db.refresh(db_questionario_cuidador)
    return db_questionario_cuidador


def update_questionario(db: Session, id_questionario: int, questionario: QuestionarioCuidadorUpdate):
    db_questionario_cuidador = db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_questionario == id_questionario).first()
    if db_questionario_cuidador:
        for key, value in questionario.dict(exclude_unset=True).items():
            setattr(db_questionario_cuidador, key, value)
        db.commit()
        db.refresh(db_questionario_cuidador)
    return db_questionario_cuidador

def delete_questionario(db: Session, id_questionario: int):
    db_questionario_cuidador = db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_questionario == id_questionario).first()
    if db_questionario_cuidador is None:
        return None
    db.delete(db_questionario_cuidador)
    db.commit()
    return db_questionario_cuidador
