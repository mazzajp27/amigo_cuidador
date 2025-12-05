from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from app.models.mensagem import Conversa, Mensagem
from app.models.contratante import Contratante
from app.models.cuidador import Cuidador
from app.schemas.mensagem import ConversaCreate, MensagemCreate, MensagemResponse

def criar_ou_buscar_conversa(db: Session, id_contratante: int, id_cuidador: int):
    """Cria uma nova conversa ou retorna a existente entre contratante e cuidador"""
    # Verificar se já existe uma conversa
    conversa = db.query(Conversa).filter(
        and_(
            Conversa.id_contratante == id_contratante,
            Conversa.id_cuidador == id_cuidador
        )
    ).first()
    
    if not conversa:
        # Criar nova conversa
        conversa = Conversa(
            id_contratante=id_contratante,
            id_cuidador=id_cuidador
        )
        db.add(conversa)
        db.commit()
        db.refresh(conversa)
    
    return conversa

def criar_mensagem(db: Session, mensagem: MensagemCreate):
    """Cria uma nova mensagem"""
    db_mensagem = Mensagem(
        id_conversa=mensagem.id_conversa,
        id_remetente=mensagem.id_remetente,
        tipo_remetente=mensagem.tipo_remetente,
        texto=mensagem.texto
    )
    db.add(db_mensagem)
    db.commit()
    db.refresh(db_mensagem)
    return db_mensagem

def buscar_conversas_por_contratante(db: Session, id_contratante: int):
    """Busca todas as conversas de um contratante"""
    conversas = db.query(Conversa).filter(
        Conversa.id_contratante == id_contratante
    ).all()
    
    resultado = []
    for conversa in conversas:
        # Buscar informações do cuidador
        cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == conversa.id_cuidador).first()
        
        # Buscar última mensagem
        ultima_mensagem_obj = db.query(Mensagem).filter(
            Mensagem.id_conversa == conversa.id_conversa
        ).order_by(Mensagem.created_at.desc()).first()
        
        # Converter última mensagem para schema se existir
        ultima_mensagem = None
        if ultima_mensagem_obj:
            ultima_mensagem = MensagemResponse(
                id_mensagem=ultima_mensagem_obj.id_mensagem,
                id_conversa=ultima_mensagem_obj.id_conversa,
                id_remetente=ultima_mensagem_obj.id_remetente,
                tipo_remetente=ultima_mensagem_obj.tipo_remetente,
                texto=ultima_mensagem_obj.texto,
                lida=ultima_mensagem_obj.lida,
                created_at=ultima_mensagem_obj.created_at
            )
        
        # Contar mensagens não lidas (mensagens enviadas pelo outro usuário)
        mensagens_nao_lidas = db.query(Mensagem).filter(
            and_(
                Mensagem.id_conversa == conversa.id_conversa,
                Mensagem.tipo_remetente == 'cuidador',  # Mensagens do cuidador para o contratante
                Mensagem.lida == False
            )
        ).count()
        
        # Contar total de mensagens
        total_mensagens = db.query(Mensagem).filter(
            Mensagem.id_conversa == conversa.id_conversa
        ).count()
        
        # Buscar nome do contratante
        contratante = db.query(Contratante).filter(Contratante.id_contratante == conversa.id_contratante).first()
        
        resultado.append({
            'id_conversa': conversa.id_conversa,
            'id_contratante': conversa.id_contratante,
            'id_cuidador': conversa.id_cuidador,
            'nome_contratante': contratante.nome if contratante else 'Contratante',
            'nome_cuidador': cuidador.nome if cuidador else 'Cuidador',
            'created_at': conversa.created_at,
            'ultima_mensagem': ultima_mensagem,
            'total_mensagens': total_mensagens,
            'mensagens_nao_lidas': mensagens_nao_lidas
        })
    
    return resultado

def buscar_conversas_por_cuidador(db: Session, id_cuidador: int):
    """Busca todas as conversas de um cuidador"""
    conversas = db.query(Conversa).filter(
        Conversa.id_cuidador == id_cuidador
    ).all()
    
    resultado = []
    for conversa in conversas:
        # Buscar informações do contratante
        contratante = db.query(Contratante).filter(Contratante.id_contratante == conversa.id_contratante).first()
        
        # Buscar última mensagem
        ultima_mensagem_obj = db.query(Mensagem).filter(
            Mensagem.id_conversa == conversa.id_conversa
        ).order_by(Mensagem.created_at.desc()).first()
        
        # Converter última mensagem para schema se existir
        ultima_mensagem = None
        if ultima_mensagem_obj:
            ultima_mensagem = MensagemResponse(
                id_mensagem=ultima_mensagem_obj.id_mensagem,
                id_conversa=ultima_mensagem_obj.id_conversa,
                id_remetente=ultima_mensagem_obj.id_remetente,
                tipo_remetente=ultima_mensagem_obj.tipo_remetente,
                texto=ultima_mensagem_obj.texto,
                lida=ultima_mensagem_obj.lida,
                created_at=ultima_mensagem_obj.created_at
            )
        
        # Contar mensagens não lidas (mensagens enviadas pelo outro usuário)
        mensagens_nao_lidas = db.query(Mensagem).filter(
            and_(
                Mensagem.id_conversa == conversa.id_conversa,
                Mensagem.tipo_remetente == 'contratante',  # Mensagens do contratante para o cuidador
                Mensagem.lida == False
            )
        ).count()
        
        # Contar total de mensagens
        total_mensagens = db.query(Mensagem).filter(
            Mensagem.id_conversa == conversa.id_conversa
        ).count()
        
        # Buscar nome do cuidador
        cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == conversa.id_cuidador).first()
        
        resultado.append({
            'id_conversa': conversa.id_conversa,
            'id_contratante': conversa.id_contratante,
            'id_cuidador': conversa.id_cuidador,
            'nome_contratante': contratante.nome if contratante else 'Contratante',
            'nome_cuidador': cuidador.nome if cuidador else 'Cuidador',
            'created_at': conversa.created_at,
            'ultima_mensagem': ultima_mensagem,
            'total_mensagens': total_mensagens,
            'mensagens_nao_lidas': mensagens_nao_lidas
        })
    
    return resultado

def buscar_mensagens_por_conversa(db: Session, id_conversa: int):
    """Busca todas as mensagens de uma conversa"""
    return db.query(Mensagem).filter(
        Mensagem.id_conversa == id_conversa
    ).order_by(Mensagem.created_at.asc()).all()

def marcar_mensagens_como_lidas(db: Session, id_conversa: int, tipo_usuario: str):
    """Marca mensagens como lidas (mensagens enviadas pelo outro usuário)"""
    tipo_remetente = 'cuidador' if tipo_usuario == 'contratante' else 'contratante'
    
    db.query(Mensagem).filter(
        and_(
            Mensagem.id_conversa == id_conversa,
            Mensagem.tipo_remetente == tipo_remetente,
            Mensagem.lida == False
        )
    ).update({Mensagem.lida: True})
    db.commit()

def buscar_conversa_por_ids(db: Session, id_contratante: int, id_cuidador: int):
    """Busca uma conversa específica entre contratante e cuidador"""
    return db.query(Conversa).filter(
        and_(
            Conversa.id_contratante == id_contratante,
            Conversa.id_cuidador == id_cuidador
        )
    ).first()

