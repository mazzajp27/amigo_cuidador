from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Conversa(Base):
    __tablename__ = "conversa"
    
    id_conversa = Column(Integer, primary_key=True, autoincrement=True)
    id_contratante = Column(Integer, ForeignKey('contratante.id_contratante'), nullable=False)
    id_cuidador = Column(Integer, ForeignKey('cuidador.id_cuidador'), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    contratante = relationship("Contratante", back_populates="conversas")
    cuidador = relationship("Cuidador", back_populates="conversas")
    mensagens = relationship("Mensagem", back_populates="conversa", cascade="all, delete-orphan", order_by="Mensagem.created_at")

class Mensagem(Base):
    __tablename__ = "mensagem"
    
    id_mensagem = Column(Integer, primary_key=True, autoincrement=True)
    id_conversa = Column(Integer, ForeignKey('conversa.id_conversa'), nullable=False)
    id_remetente = Column(Integer, nullable=False)  # ID do remetente (contratante ou cuidador)
    tipo_remetente = Column(String(20), nullable=False)  # 'contratante' ou 'cuidador'
    texto = Column(String, nullable=False)
    lida = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    conversa = relationship("Conversa", back_populates="mensagens")

