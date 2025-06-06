"""Initial migration

Revision ID: b2a5631bff88
Revises: 
Create Date: 2025-06-02 15:46:06.407734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = 'b2a5631bff88'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create tables in correct order with proper transaction handling
    
    # First, create the contratante table
    op.execute("""
    DROP TABLE IF EXISTS contratante CASCADE;
    CREATE TABLE contratante (
        id_contratante SERIAL PRIMARY KEY,
        nome VARCHAR NOT NULL,
        cpf VARCHAR(14) UNIQUE,
        email VARCHAR UNIQUE,
        telefone VARCHAR,
        telefone_emergencia VARCHAR,
        senha VARCHAR,
        genero VARCHAR,
        data_nascimento DATE
    );
    """)
    
    # Verify contratante table exists before creating dependent tables
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    tables = inspector.get_table_names()
    
    if 'contratante' not in tables:
        raise Exception("contratante table was not created successfully")
        
    # Now create the dependent tables
    op.create_table('endereco',
        sa.Column('id_endereco', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('cep', sa.String(length=8), nullable=False),
        sa.Column('endereco', sa.String(), nullable=False),
        sa.Column('numero', sa.String(), nullable=False),
        sa.Column('complemento', sa.String(), nullable=True),
        sa.Column('bairro', sa.String(), nullable=False),
        sa.Column('cidade', sa.String(), nullable=False),
        sa.Column('estado', sa.String(length=2), nullable=False),
        sa.Column('referencia', sa.String(), nullable=True),
        sa.Column('id_contratante', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_contratante'], ['contratante.id_contratante'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id_endereco')
    )
    
    op.create_table('hobbies',
        sa.Column('id_hobbie', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('atividades_gosta', sa.String(), nullable=False),
        sa.Column('pratica_esporte', sa.String(length=3), nullable=False),
        sa.Column('esporte_praticado', sa.String(), nullable=False),
        sa.Column('atividades_manuais', sa.String(length=3), nullable=False),
        sa.Column('atividades_manuais_praticadas', sa.String(), nullable=False),
        sa.Column('interesse_aprender', sa.String(length=3), nullable=False),
        sa.Column('interesse_aprender_especifico', sa.String(), nullable=False),
        sa.Column('gerenero_musical', sa.String(), nullable=False),
        sa.Column('filmes_tv', sa.String(), nullable=False),
        sa.Column('participa_eventos', sa.String(length=3), nullable=False),
        sa.Column('eventos', sa.String(), nullable=False),
        sa.Column('ensina', sa.String(length=3), nullable=False),
        sa.Column('ensinamentos_passados', sa.String(), nullable=False),
        sa.Column('atividades_tecnologicas', sa.String(length=3), nullable=False),
        sa.Column('atividades_tecnologicas_praticadas', sa.String(), nullable=False),
        sa.Column('outros_hobbies', sa.String(), nullable=False),
        sa.Column('id_contratante', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_contratante'], ['contratante.id_contratante'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id_hobbie')
    )
    
    op.create_table('questionario',
        sa.Column('id_questionario', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('possui_condicao_medica', sa.String(length=3), nullable=False),
        sa.Column('condicao_medica', sa.String(), nullable=False),
        sa.Column('toma_medicamento', sa.String(length=3), nullable=False),
        sa.Column('medicamento', sa.String(), nullable=False),
        sa.Column('realiza_atividades_diarias', sa.String(length=3), nullable=False),
        sa.Column('atividades_diarias_ajuda', sa.String(), nullable=False),
        sa.Column('familia_apoio', sa.String(length=3), nullable=False),
        sa.Column('frequencia_visitas', sa.String(), nullable=False),
        sa.Column('principais_qualidades_preferencias', sa.String(), nullable=True),
        sa.Column('espera_cuidador', sa.String(), nullable=False),
        sa.Column('possui_deficiencias', sa.String(length=3), nullable=False),
        sa.Column('deficiencias', sa.String(), nullable=False),
        sa.Column('observacoes', sa.String(), nullable=True),
        sa.Column('id_contratante', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['id_contratante'], ['contratante.id_contratante'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id_questionario')
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Drop tables in reverse order
    op.execute("""
    DROP TABLE IF EXISTS questionario CASCADE;
    DROP TABLE IF EXISTS hobbies CASCADE;
    DROP TABLE IF EXISTS endereco CASCADE;
    DROP TABLE IF EXISTS contratante CASCADE;
    """)
