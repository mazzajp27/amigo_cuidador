# app/crud/contratante.py

from sqlalchemy.orm import Session
from app.models.contratante import Contratante
from app.schemas.contratante import ContratanteCreate, ContratanteUpdate
from app.models.endereco import Endereco
from app.models.questionario import Questionario
from app.models.hobbies import Hobbies

def create_contratante(db: Session, contratante: ContratanteCreate):
    # Extrair dados do contratante (sem os campos relacionados)
    # Usar dict(exclude_unset=False) para garantir que todos os campos sejam incluídos
    contratante_dict = contratante.dict(exclude_unset=False)
    
    # Debug: verificar o que está chegando
    import json
    print(f"DEBUG - contratante_dict completo: {json.dumps(contratante_dict, indent=2, default=str)}")
    print(f"DEBUG - Chaves no contratante_dict: {list(contratante_dict.keys())}")
    
    # Campos relacionados que serão processados separadamente
    endereco_data = {
        'estado': contratante_dict.pop('estado', None),
        'cidade': contratante_dict.pop('cidade', None),
        'endereco': contratante_dict.pop('endereco', None),
        'bairro': contratante_dict.pop('bairro', None),
        'cep': contratante_dict.pop('cep', None),
        'numero': contratante_dict.pop('numero', None),
        'complemento': contratante_dict.pop('complemento', None),
        'referencia': contratante_dict.pop('referencia', None),
    }
    
    questionario_data = contratante_dict.pop('questionario', None)
    hobbies_list = contratante_dict.pop('hobbies', None)
    atividades_fisicas = contratante_dict.pop('atividadesFisicas', None)
    atividades_sociais = contratante_dict.pop('atividadesSociais', None)
    preferencias = contratante_dict.pop('preferencias', None)
    
    print(f"DEBUG - hobbies_list extraído: {hobbies_list}")
    print(f"DEBUG - atividades_fisicas: {atividades_fisicas}")
    print(f"DEBUG - atividades_sociais: {atividades_sociais}")
    print(f"DEBUG - preferencias: {preferencias}")
    
    # Converter data_nascimento se vier como string
    if 'data_nascimento' in contratante_dict and isinstance(contratante_dict['data_nascimento'], str):
        from datetime import datetime
        try:
            contratante_dict['data_nascimento'] = datetime.strptime(contratante_dict['data_nascimento'], '%Y-%m-%d').date()
        except:
            contratante_dict['data_nascimento'] = None
    
    # Criar o contratante
    db_contratante = Contratante(**contratante_dict)
    db.add(db_contratante)
    db.commit()
    db.refresh(db_contratante)
    
    # Criar endereço se houver dados
    if any(endereco_data.values()):
        endereco_data['id_contratante'] = db_contratante.id_contratante
        # Remover None values
        endereco_data = {k: v for k, v in endereco_data.items() if v is not None}
        if endereco_data.get('estado') and endereco_data.get('cidade') and endereco_data.get('endereco'):
            db_endereco = Endereco(**endereco_data)
            db.add(db_endereco)
    
    # Criar questionário (sempre criar, mesmo que vazio)
    saude_geral = questionario_data.get('saudeGeral', {}) if questionario_data else {}
    necessidades = questionario_data.get('necessidadesCuidado', {}) if questionario_data else {}
    preferencias_cuidado = questionario_data.get('preferenciasCuidado', {}) if questionario_data else {}
    
    auxilio_diarias = necessidades.get('auxilioAtividadesDiarias', {})
    auxilio_med = necessidades.get('auxilioMedicacao', {})
    monitoramento = necessidades.get('monitoramentoSinais', {})
    
    questionario_create = {
        'id_contratante': db_contratante.id_contratante,
        'condicao_medica': saude_geral.get('condicoesMedicas', '') or None,
        'medicamento': saude_geral.get('medicamentosUso', '') or None,
        'alergia': saude_geral.get('alergias', '') or None,
        'restricao_alimentar': saude_geral.get('restricoesAlimentares', '') or None,
        'restricao_mobilidade': saude_geral.get('mobilidadeRestricoes', '') or None,
        'auxilio_atividades_diarias': 'Sim' if auxilio_diarias.get('precisa') else 'Não',
        'auxilio_medicacao': 'Sim' if auxilio_med.get('precisa') else 'Não',
        'monitoramento_sinais_vitais': 'Sim' if monitoramento.get('necessario') else 'Não',
        'horario_preferencia': preferencias_cuidado.get('horarioPreferencial', '') or None,
        'frequencia_cuidado': preferencias_cuidado.get('frequenciaCuidado', '') or None,
        'caracteristicas_cuidador': preferencias_cuidado.get('caracteristicasCuidador', '') or None,
        'observacoes': preferencias_cuidado.get('observacoesAdicionais', '') or None,
    }
    db_questionario = Questionario(**questionario_create)
    db.add(db_questionario)
    
    # Criar hobbies (sempre criar, mesmo que vazio)
    # Converter hobbies_list para string se for array
    hobbies_str = 'Não informado'
    if hobbies_list:
        if isinstance(hobbies_list, list):
            if len(hobbies_list) > 0:
                hobbies_str = ', '.join(str(h) for h in hobbies_list)
        elif isinstance(hobbies_list, str):
            hobbies_str = hobbies_list if hobbies_list.strip() else 'Não informado'
    
    # Processar atividades físicas
    pratica_esporte = 'Não'
    esporte_praticado = ''
    if atividades_fisicas:
        if isinstance(atividades_fisicas, dict):
            if atividades_fisicas.get('pratica'):
                pratica_esporte = 'Sim'
                esporte_praticado = atividades_fisicas.get('quais', '') or ''
    
    # Processar atividades sociais
    participa_eventos = 'Não'
    eventos = ''
    if atividades_sociais:
        if isinstance(atividades_sociais, dict):
            if atividades_sociais.get('participa'):
                participa_eventos = 'Sim'
                eventos = atividades_sociais.get('quais', '') or ''
    
    # Processar preferências
    outros_hobbies = ''
    if preferencias:
        if isinstance(preferencias, dict):
            outros_hobbies = preferencias.get('observacoesAdicionais', '') or ''
    
    hobbies_create = {
        'id_contratante': db_contratante.id_contratante,
        'atividades_gosta': hobbies_str,
        'pratica_esporte': pratica_esporte,
        'esporte_praticado': esporte_praticado,
        'atividades_manuais': 'Não',
        'atividades_manuais_praticadas': '',
        'interesse_aprender': 'Não',
        'interesse_aprender_especifico': '',
        'gerenero_musical': '',
        'filmes_tv': '',
        'participa_eventos': participa_eventos,
        'eventos': eventos,
        'ensina': 'Não',
        'ensinamentos_passados': '',
        'atividades_tecnologicas': 'Não',
        'atividades_tecnologicas_praticadas': '',
        'outros_hobbies': outros_hobbies,
    }
    print(f"DEBUG - hobbies_data final: {hobbies_create}")
    db_hobbies = Hobbies(**hobbies_create)
    db.add(db_hobbies)
    print(f"DEBUG - Hobbies criado com sucesso, ID: {db_hobbies.id_hobbie}")
    
    db.commit()
    db.refresh(db_contratante)
    return db_contratante


def get_contratantes(db: Session):
    return db.query(Contratante).all()


def get_contratante(db: Session, id_contratante: int):
    return db.query(Contratante).filter(Contratante.id_contratante == id_contratante).first()


def update_contratante(db: Session, id_contratante: int, contratante: ContratanteUpdate):
    db_contratante = db.query(Contratante).filter(Contratante.id_contratante == id_contratante).first()
    if db_contratante:
        for key, value in contratante.dict(exclude_unset=True).items():
            setattr(db_contratante, key, value)
        db.commit()
        db.refresh(db_contratante)
    return db_contratante


def delete_contratante(db: Session, id_contratante: int):
    db_contratante = db.query(Contratante).filter(Contratante.id_contratante == id_contratante).first()
    if db_contratante is None:
        return None
    db.delete(db_contratante)
    db.commit()
    return db_contratante