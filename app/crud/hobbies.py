from sqlalchemy.orm import Session
from app.models.hobbies import Hobbies
from app.schemas.hobbies import HobbiesCreate, HobbiesUpdate

def get_hobbie(db: Session, id_hobbies: int):
    return db.query(Hobbies).filter(Hobbies.id_hobbie == id_hobbies).first()


def get_hobbies(db: Session):
    return db.query(Hobbies).all()

def get_hobbies_pelo_contratante(db: Session, id_contratante: int):
    return db.query(Hobbies).filter(Hobbies.id_contratante == id_contratante).all()


def create_hobbie(db: Session, hobbies: HobbiesCreate):
    db_hobbie = Hobbies(**hobbies.dict())
    db.add(db_hobbie)
    db.commit()
    db.refresh(db_hobbie)
    return db_hobbie

def update_hobbie(db: Session, id_hobbies: int, hobbies: HobbiesUpdate):
    db_hobbie = db.query(Hobbies).filter(Hobbies.id_hobbie == id_hobbies).first()
    if db_hobbie:
        for key, value in hobbies.dict(exclude_unset=True).items():
            setattr(db_hobbie, key, value)
        db.commit()
        db.refresh(db_hobbie)
    return db_hobbie
        
def delete_hobbie(db: Session, id_hobbies: int):
    db_hobbie = db.query(Hobbies).filter(Hobbies.id_hobbie == id_hobbies).first()
    if db_hobbie is None:
        return None
    db.delete(db_hobbie)
    db.commit()
    return db_hobbie 

