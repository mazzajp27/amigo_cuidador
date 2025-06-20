from sqlalchemy.orm import Session
from app.models.hobbies_cuidador import HobbiesCuidador
from app.schemas.hobbies_cuidador import HobbiesCuidadorCreate, HobbiesCuidadorUpdate

def get_hobbie(db: Session, id_hobbies_cuidador: int):
    return db.query(HobbiesCuidador).filter(HobbiesCuidador.id_hobbies_cuidador == id_hobbies_cuidador).first()


def get_hobbies(db: Session):
    return db.query(HobbiesCuidador).all()


def get_hobbies_pelo_cuidador(db: Session, id_cuidador: int):
    return db.query(HobbiesCuidador).filter(HobbiesCuidador.id_cuidador == id_cuidador).all()


def create_hobbie(db: Session, hobbies: HobbiesCuidadorCreate):
    db_hobbie = HobbiesCuidador(**hobbies.dict())
    db.add(db_hobbie)
    db.commit()
    db.refresh(db_hobbie)
    return db_hobbie

def update_hobbie(db: Session, id_hobbies_cuidador: int, hobbies: HobbiesCuidadorUpdate):
    db_hobbie = db.query(HobbiesCuidador).filter(HobbiesCuidador.id_hobbies_cuidador == id_hobbies_cuidador).first()
    if db_hobbie:
        for key, value in hobbies.dict(exclude_unset=True).items():
            setattr(db_hobbie, key, value)  
        db.commit()
        db.refresh(db_hobbie)
    return db_hobbie
        
def delete_hobbie(db: Session, id_hobbies_cuidador: int):
    db_hobbie = db.query(HobbiesCuidador).filter(HobbiesCuidador.id_hobbies_cuidador == id_hobbies_cuidador).first()
    if db_hobbie is None:
        return None
    db.delete(db_hobbie)
    db.commit()
    return db_hobbie 

