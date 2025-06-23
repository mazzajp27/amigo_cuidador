from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class EnderecoCuidador(Base):
    __tablename__ = "endereco_cuidador"

    id_endereco_cuidador = Column(Integer, primary_key=True, autoincrement=True)
    cep = Column(String(8), nullable=False)
    endereco = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    complemento = Column(String)
    bairro = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    estado = Column(String(2), nullable=False)
    referencia = Column(String)

    # Foreign key relationship with Cuidador
    id_cuidador = Column(Integer, ForeignKey('cuidador.id_cuidador'), nullable=False)
    cuidador = relationship("Cuidador", back_populates="enderecos") 