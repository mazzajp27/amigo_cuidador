from sqlalchemy.orm import Session, joinedload
from app.models.cuidador import Cuidador
from app.models.usuario import Usuario
from app.schemas.cuidador import CuidadorCreate, CuidadorUpdate

def create_cuidador(db: Session, cuidador: CuidadorCreate, usuario_id: int = None):
    if usuario_id is None:
        raise ValueError("usuario_id é obrigatório para criar um cuidador")
    
    db_cuidador = Cuidador(id_cuidador=usuario_id)
    db.add(db_cuidador)
    db.commit()
    db.refresh(db_cuidador)
    return db_cuidador

def get_cuidadores(db: Session):
    return db.query(Cuidador).all()

def get_cuidador(db: Session, id_cuidador: int):
    return db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()

def get_cuidador_by_email(db: Session, email: str):
    return db.query(Cuidador).join(Cuidador.usuario).filter(Usuario.email == email).first()

def get_cuidador_by_cpf(db: Session, cpf: str):
    return db.query(Cuidador).join(Cuidador.usuario).filter(Usuario.cpf == cpf).first()

def update_cuidador(db: Session, id_cuidador: int, cuidador: CuidadorUpdate):
    db_cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()
    if db_cuidador:
        # Atualiza os dados do usuário
        for key, value in cuidador.dict(exclude_unset=True).items():
            setattr(db_cuidador.usuario, key, value)
        db.commit()
        db.refresh(db_cuidador)
        return db_cuidador
    return None

def delete_cuidador(db: Session, id_cuidador: int):
    db_cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()
    if db_cuidador is None:
        return None
    db.delete(db_cuidador)
    db.commit()
    return db_cuidador 