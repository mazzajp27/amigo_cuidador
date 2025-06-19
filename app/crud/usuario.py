from sqlalchemy.orm import Session
from app.models.usuario import Usuario, TipoUsuario
from app.models.contratante import Contratante
from app.models.cuidador import Cuidador
from app.schemas.usuario import UsuarioCreate

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    
    # Se o tipo de usuário for contratante, cria o registro na tabela contratante
    if usuario.tipo_usuario == TipoUsuario.CONTRATANTE:
        db_contratante = Contratante(id_contratante=db_usuario.id_usuario)
        db.add(db_contratante)
        db.commit()
        db.refresh(db_contratante)
    # Se o tipo de usuário for cuidador, cria o registro na tabela cuidador
    elif usuario.tipo_usuario == TipoUsuario.CUIDADOR:
        db_cuidador = Cuidador(id_cuidador=db_usuario.id_usuario)
        db.add(db_cuidador)
        db.commit()
        db.refresh(db_cuidador)
    
    return db_usuario

def get_usuario_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

def get_usuario_by_cpf(db: Session, cpf: str):
    return db.query(Usuario).filter(Usuario.cpf == cpf).first() 