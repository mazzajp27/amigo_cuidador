from sqlalchemy.orm import Session
from app.models.endereco import Endereco
from app.schemas.endereco import EnderecoCreate, EnderecoUpdate

def create_endereco(db: Session, endereco: EnderecoCreate):
    db_endereco = Endereco(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco

def get_enderecos(db: Session, id_contratante: int):
    return db.query(Endereco).filter(Endereco.id_contratante == id_contratante).all()

def get_endereco(db: Session, id_endereco: int):
    return db.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()

def update_endereco(db: Session, id_endereco: int, endereco: EnderecoUpdate):
    db_endereco = db.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()
    if db_endereco:
        for key, value in endereco.dict(exclude_unset=True).items():
            setattr(db_endereco, key, value)
        db.commit()
        db.refresh(db_endereco)
    return db_endereco

def delete_endereco(db: Session, id_endereco: int):
    db_endereco = db.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()
    if db_endereco is None:
        return None
    db.delete(db_endereco)
    db.commit()
    return db_endereco 