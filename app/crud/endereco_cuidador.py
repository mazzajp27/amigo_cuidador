from sqlalchemy.orm import Session
from app.models.endereco_cuidador import EnderecoCuidador
from app.schemas.endereco_cuidador import EnderecoCuidadorCreate, EnderecoCuidadorUpdate


def get_endereco(db: Session, id_endereco_cuidador: int):
    return db.query(EnderecoCuidador).filter(EnderecoCuidador.id_endereco_cuidador == id_endereco_cuidador).first()


def get_enderecos(db: Session):
    return db.query(EnderecoCuidador).all()


def get_enderecos_pelo_cuidador(db: Session, id_cuidador: int):
    return db.query(EnderecoCuidador).filter(EnderecoCuidador.id_cuidador == id_cuidador).all()


def create_endereco(db: Session, endereco: EnderecoCuidadorCreate):
    db_endereco = EnderecoCuidador(**endereco.dict())
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco


def update_endereco(db: Session, id_endereco_cuidador: int, endereco: EnderecoCuidadorUpdate):
    db_endereco = db.query(EnderecoCuidador).filter(EnderecoCuidador.id_endereco_cuidador == id_endereco_cuidador).first()
    if db_endereco:
        for key, value in endereco.dict(exclude_unset=True).items():
            setattr(db_endereco, key, value)
        db.commit()
        db.refresh(db_endereco)
    return db_endereco


def delete_endereco(db: Session, id_endereco_cuidador: int):
    db_endereco = db.query(EnderecoCuidador).filter(EnderecoCuidador.id_endereco_cuidador == id_endereco_cuidador).first()
    if db_endereco is None:
        return None
    db.delete(db_endereco)
    db.commit()
    return db_endereco 