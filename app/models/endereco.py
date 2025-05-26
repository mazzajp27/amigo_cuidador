from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Endereco(Base):
    __tablename__ = "endereco"

    id_endereco = Column(Integer, primary_key=True, autoincrement=True)
    cep = Column(String(8), nullable=False)
    endereco = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    complemento = Column(String)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String(2), nullable=False)
    referencia = Column(String)

    # Foreign key relationship with Contratante
    id_contratante = Column(Integer, ForeignKey('contratante.id_contratante'), nullable=False)
    contratante = relationship("Contratante", back_populates="enderecos") 