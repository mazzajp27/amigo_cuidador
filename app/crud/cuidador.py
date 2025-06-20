# app/crud/contratante.py

from sqlalchemy.orm import Session
from app.models.cuidador import Cuidador
from app.schemas.cuidador import CuidadorCreate, CuidadorUpdate

def create_cuidador(db: Session, cuidador: CuidadorCreate):
    db_cuidador = Cuidador(**cuidador.dict())
    db.add(db_cuidador)
    db.commit()
    db.refresh(db_cuidador)
    return db_cuidador


def get_cuidadores(db: Session):
    return db.query(Cuidador).all()


def get_cuidador(db: Session, id_cuidador: int):
    return db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()


def update_cuidador(db: Session, id_cuidador: int, cuidador: CuidadorUpdate):
    db_cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()
    if db_cuidador:
        for key, value in cuidador.dict(exclude_unset=True).items():
            setattr(db_cuidador, key, value)
        db.commit()
        db.refresh(db_cuidador)
    return db_cuidador


def delete_cuidador(db: Session, id_cuidador: int):
    db_cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()
    if db_cuidador is None:
        return None
    db.delete(db_cuidador)
    db.commit()
    return db_cuidador