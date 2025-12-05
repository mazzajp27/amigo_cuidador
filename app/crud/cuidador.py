# app/crud/cuidador.py

from sqlalchemy.orm import Session
from app.models.cuidador import Cuidador
from app.schemas.cuidador import CuidadorCreate, CuidadorUpdate
from app.models.endereco_cuidador import EnderecoCuidador
from app.models.questionario_cuidador import QuestionarioCuidador
from app.models.hobbies_cuidador import HobbiesCuidador

def create_cuidador(db: Session, cuidador: CuidadorCreate):
    # Extrair dados do cuidador (sem os campos relacionados)
    # Usar dict(exclude_unset=False) para garantir que todos os campos sejam incluídos
    cuidador_dict = cuidador.dict(exclude_unset=False)
    
    # Debug: verificar o que está chegando
    import json
    print(f"DEBUG - cuidador_dict completo: {json.dumps(cuidador_dict, indent=2, default=str)}")
    print(f"DEBUG - Chaves no cuidador_dict: {list(cuidador_dict.keys())}")
    
    # Campos relacionados que serão processados separadamente
    endereco_data = {
        'estado': cuidador_dict.pop('estado', None),
        'cidade': cuidador_dict.pop('cidade', None),
        'endereco': cuidador_dict.pop('endereco', None),
        'bairro': cuidador_dict.pop('bairro', None),
        'cep': cuidador_dict.pop('cep', None),
        'numero': cuidador_dict.pop('numero', None),
        'complemento': cuidador_dict.pop('complemento', None),
        'referencia': cuidador_dict.pop('referencia', None),
    }
    
    formacao_academica = cuidador_dict.pop('formacaoAcademica', None)
    experiencia_profissional = cuidador_dict.pop('experienciaProfissional', None)
    qualidades = cuidador_dict.pop('qualidades', None)
    referencias = cuidador_dict.pop('referencias', None)
    interesses = cuidador_dict.pop('interesses', None)
    
    print(f"DEBUG - interesses extraído: {interesses}")
    print(f"DEBUG - formacao_academica: {formacao_academica}")
    print(f"DEBUG - experiencia_profissional: {experiencia_profissional}")
    
    # Converter data_nascimento se vier como string
    if 'data_nascimento' in cuidador_dict and isinstance(cuidador_dict['data_nascimento'], str):
        from datetime import datetime
        try:
            cuidador_dict['data_nascimento'] = datetime.strptime(cuidador_dict['data_nascimento'], '%Y-%m-%d').date()
        except:
            cuidador_dict['data_nascimento'] = None
    
    # Criar o cuidador
    db_cuidador = Cuidador(**cuidador_dict)
    db.add(db_cuidador)
    db.commit()
    db.refresh(db_cuidador)
    
    # Criar endereço se houver dados
    if any(endereco_data.values()):
        endereco_data['id_cuidador'] = db_cuidador.id_cuidador
        # Remover None values
        endereco_data = {k: v for k, v in endereco_data.items() if v is not None}
        if endereco_data.get('estado') and endereco_data.get('cidade') and endereco_data.get('endereco'):
            db_endereco = EnderecoCuidador(**endereco_data)
            db.add(db_endereco)
    
    # Criar questionário (sempre criar, mesmo que vazio)
    questionario_data = {
        'id_cuidador': db_cuidador.id_cuidador,
        'cursos_realizados': formacao_academica.get('cursos', 'Não informado') if formacao_academica else 'Não informado',
        'instituicao_ensino': formacao_academica.get('instituicao', 'Não informado') if formacao_academica else 'Não informado',
        'area_formacao': formacao_academica.get('area', 'Não informado') if formacao_academica else 'Não informado',
        'tempo_experiencia': experiencia_profissional.get('tempoExperiencia', 'Não informado') if experiencia_profissional else 'Não informado',
        'principais_responsabilidades': experiencia_profissional.get('responsabilidades', 'Não informado') if experiencia_profissional else 'Não informado',
        'possui_certificacao': 'Sim' if (experiencia_profissional and experiencia_profissional.get('possuiCertificacao')) else 'Não',
        'certificacao': experiencia_profissional.get('certificacoes', 'Não informado') if experiencia_profissional else 'Não informado',
        'qualidades_preferencias': qualidades.get('qualidadesImportantes', 'Não informado') if qualidades else 'Não informado',
        'horario_disponivel': qualidades.get('horariosDisponiveis', 'Não informado') if qualidades else 'Não informado',
        'disponibilidade_plantao': 'Sim' if (qualidades and qualidades.get('disponibilidadePlantoes')) else 'Não',
        'qualidades_cuidador': ', '.join(qualidades.get('habilidades', [])) if qualidades and qualidades.get('habilidades') else 'Não informado',
        'referencia_cuidador': referencias.get('nomeContato', 'Não informado') if referencias else 'Não informado',
    }
    db_questionario = QuestionarioCuidador(**questionario_data)
    db.add(db_questionario)
    
    # Criar hobbies (sempre criar, mesmo que vazio)
    # Debug: imprimir o que está sendo recebido
    import json
    print(f"DEBUG - interesses recebido: {json.dumps(interesses, indent=2, default=str) if interesses else 'None'}")
    print(f"DEBUG - tipo de interesses: {type(interesses)}")
    
    # Processar atividades que gosta
    atividades_gosta = 'Não informado'
    if interesses and isinstance(interesses, dict):
        atividades_tempo = interesses.get('atividadesTempo')
        print(f"DEBUG - atividadesTempo: {atividades_tempo}, tipo: {type(atividades_tempo)}")
        if atividades_tempo:
            if isinstance(atividades_tempo, list) and len(atividades_tempo) > 0:
                atividades_gosta = ', '.join(str(a) for a in atividades_tempo if a)
                print(f"DEBUG - atividades_gosta processado: {atividades_gosta}")
    
    # Processar atividades manuais
    atividades_manuais = 'Não'
    if interesses and isinstance(interesses, dict):
        atividades_manuais_obj = interesses.get('atividadesManuais')
        print(f"DEBUG - atividadesManuais: {atividades_manuais_obj}")
        if atividades_manuais_obj and isinstance(atividades_manuais_obj, dict):
            if atividades_manuais_obj.get('gosta'):
                atividades_manuais = 'Sim'
                quais = atividades_manuais_obj.get('quais', '').strip()
                if quais:
                    atividades_manuais = f"Sim - {quais}"
    
    # Processar preferências culturais
    pref_culturais = {}
    if interesses and isinstance(interesses, dict):
        pref_culturais = interesses.get('prefCulturais', {})
        if not isinstance(pref_culturais, dict):
            pref_culturais = {}
    
    genero_musical = pref_culturais.get('generosMusicais', '') if isinstance(pref_culturais, dict) else ''
    genero_musical = genero_musical.strip() if genero_musical else 'Não informado'
    
    filmes_tv = pref_culturais.get('filmesTV', '') if isinstance(pref_culturais, dict) else ''
    filmes_tv = filmes_tv.strip() if filmes_tv else 'Não informado'
    
    # Processar atividades sociais
    participa_eventos = 'Não'
    if pref_culturais and isinstance(pref_culturais, dict):
        atividades_sociais_obj = pref_culturais.get('atividadesSociais', {})
        if isinstance(atividades_sociais_obj, dict) and atividades_sociais_obj.get('participa'):
            participa_eventos = 'Sim'
            quais = atividades_sociais_obj.get('quais', '').strip()
            if quais:
                participa_eventos = f"Sim - {quais}"
    
    # Processar habilidades e preferências
    habilidades_pref = {}
    if interesses and isinstance(interesses, dict):
        habilidades_pref = interesses.get('habilidadesPreferencias', {})
        if not isinstance(habilidades_pref, dict):
            habilidades_pref = {}
    
    gosta_ensinar = 'Não'
    if isinstance(habilidades_pref, dict):
        gosta_ensinar_obj = habilidades_pref.get('gostaEnsinar', {})
        if isinstance(gosta_ensinar_obj, dict) and gosta_ensinar_obj.get('gosta'):
            gosta_ensinar = 'Sim'
            oque_poderia = gosta_ensinar_obj.get('oquePoderia', '').strip()
            if oque_poderia:
                gosta_ensinar = f"Sim - {oque_poderia}"
    
    atividades_tecnologicas = 'Não'
    if isinstance(habilidades_pref, dict):
        interesse_tec_obj = habilidades_pref.get('interesseTecnologia', {})
        if isinstance(interesse_tec_obj, dict):
            is_interessado = interesse_tec_obj.get('interessado') or interesse_tec_obj.get('interesse')
            if is_interessado:
                atividades_tecnologicas = 'Sim'
                quais = interesse_tec_obj.get('quais', '').strip()
                if quais:
                    atividades_tecnologicas = f"Sim - {quais}"
    
    comentarios = ''
    if interesses and isinstance(interesses, dict):
        comentarios = interesses.get('comentarios', '')
    comentarios = comentarios.strip() if comentarios else 'Não informado'
    
    hobbies_data = {
        'id_cuidador': db_cuidador.id_cuidador,
        'atividades_gosta': atividades_gosta,
        'atividades_manuais': atividades_manuais,
        'gerenero_musical': genero_musical if genero_musical else 'Não informado',
        'filmes_tv': filmes_tv if filmes_tv else 'Não informado',
        'participa_eventos': participa_eventos,
        'gosta_ensinar': gosta_ensinar,
        'atividades_tecnologicas': atividades_tecnologicas,
        'comentarios': comentarios if comentarios else 'Não informado',
    }
    print(f"DEBUG - hobbies_data final: {hobbies_data}")
    db_hobbies = HobbiesCuidador(**hobbies_data)
    db.add(db_hobbies)
    print(f"DEBUG - HobbiesCuidador criado com sucesso, ID: {db_hobbies.id_hobbies_cuidador}")
    
    db.commit()
    db.refresh(db_cuidador)
    return db_cuidador


def get_cuidadores(db: Session):
    return db.query(Cuidador).all()


def get_cuidador(db: Session, id_cuidador: int):
    return db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()


def update_cuidador(db: Session, id_cuidador: int, cuidador: CuidadorUpdate):
    db_cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()
    if db_cuidador:
        for key, value in cuidador.dict(exclude_unset=True).items():
            setattr(db_cuidador, key, value)
        db.commit()
        db.refresh(db_cuidador)
    return db_cuidador


def delete_cuidador(db: Session, id_cuidador: int):
    db_cuidador = db.query(Cuidador).filter(Cuidador.id_cuidador == id_cuidador).first()
    if db_cuidador is None:
        return None
    db.delete(db_cuidador)
    db.commit()
    return db_cuidador