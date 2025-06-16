from sqlalchemy.orm import Session
from app.models.questionario_cuidador import QuestionarioCuidador
from app.schemas.questionario_cuidador import QuestionarioCuidadorCreate, QuestionarioCuidadorUpdate

def get_questionario_cuidador(db: Session, id_questionario_cuidador: int):
    return db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_questionario_cuidador == id_questionario_cuidador).first()

def get_questionarios_cuidador(db: Session):
    return db.query(QuestionarioCuidador).all()

def get_questionario_pelo_cuidador(db: Session, id_cuidador: int):
    return db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_cuidador == id_cuidador).all()

def create_questionario_cuidador(db: Session, questionario: QuestionarioCuidadorCreate):
    db_questionario = QuestionarioCuidador(**questionario.dict())
    db.add(db_questionario)
    db.commit()
    db.refresh(db_questionario)
    return db_questionario

def update_questionario_cuidador(db: Session, id_questionario_cuidador: int, questionario: QuestionarioCuidadorUpdate):
    db_questionario = db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_questionario_cuidador == id_questionario_cuidador).first()
    if db_questionario:
        for key, value in questionario.dict(exclude_unset=True).items():
            setattr(db_questionario, key, value)
        db.commit()
        db.refresh(db_questionario)
    return db_questionario

def delete_questionario_cuidador(db: Session, id_questionario_cuidador: int):
    db_questionario = db.query(QuestionarioCuidador).filter(QuestionarioCuidador.id_questionario_cuidador == id_questionario_cuidador).first()
    if db_questionario is None:
        return None
    db.delete(db_questionario)
    db.commit()
    return db_questionario 