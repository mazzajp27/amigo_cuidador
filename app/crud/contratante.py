# app/crud/contratante.py

from sqlalchemy.orm import Session
from app.models.contratante import Contratante
from app.schemas.contratante import ContratanteCreate, ContratanteUpdate

def create_contratante(db: Session, contratante: ContratanteCreate):
    db_contratante = Contratante(**contratante.dict())
    db.add(db_contratante)
    db.commit()
    db.refresh(db_contratante)
    return db_contratante


def get_contratantes(db: Session):
    return db.query(Contratante).all()


def get_contratante(db: Session, id_contratante: int):
    return db.query(Contratante).filter(Contratante.id_contratante == id_contratante).first()


def update_contratante(db: Session, id_contratante: int, contratante: ContratanteUpdate):
    db_contratante = db.query(Contratante).filter(Contratante.id_contratante == id_contratante).first()
    if db_contratante:
        for key, value in contratante.dict(exclude_unset=True).items():
            setattr(db_contratante, key, value)
        db.commit()
        db.refresh(db_contratante)
    return db_contratante


def delete_contratante(db: Session, id_contratante: int):
    db_contratante = db.query(Contratante).filter(Contratante.id_contratante == id_contratante).first()
    if db_contratante is None:
        return None
    db.delete(db_contratante)
    db.commit()
    return db_contratante