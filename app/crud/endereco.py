from sqlalchemy.orm import Session
from app.models.endereco import Endereco
from app.schemas.endereco import EnderecoCreate, EnderecoUpdate


def get_endereco(db: Session, id_endereco: int):
    return db.query(Endereco).filter(Endereco.id_endereco == id_endereco).first()


def get_enderecos(db: Session):
    return db.query(Endereco).all()


def get_enderecos_pelo_usuario(db: Session, usuario_id: int):
    return db.query(Endereco).filter(Endereco.usuario_id == usuario_id).all()


def create_endereco(db: Session, endereco: EnderecoCreate, usuario_id: int = None):
    data = endereco.dict()
    if usuario_id is not None:
        data['usuario_id'] = usuario_id
    db_endereco = Endereco(**data)
    db.add(db_endereco)
    db.commit()
    db.refresh(db_endereco)
    return db_endereco


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