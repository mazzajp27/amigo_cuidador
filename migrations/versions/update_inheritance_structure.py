"""update inheritance structure

Revision ID: update_inheritance_001
Revises: 773d716f95e8
Create Date: 2024-01-01 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'update_inheritance_001'
down_revision = '773d716f95e8'
branch_labels = None
depends_on = None


def upgrade():
    # Criar tabela usuarios
    op.create_table('usuarios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('cpf', sa.String(length=14), nullable=False),
        sa.Column('nome', sa.String(), nullable=False),
        sa.Column('telefone', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('senha', sa.String(), nullable=False),
        sa.Column('genero', sa.String(), nullable=False),
        sa.Column('data_nascimento', sa.Date(), nullable=False),
        sa.Column('telefone_emergencia', sa.String(), nullable=True),
        sa.Column('tipo', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('data_cadastro', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuarios_cpf'), 'usuarios', ['cpf'], unique=True)
    op.create_index(op.f('ix_usuarios_email'), 'usuarios', ['email'], unique=True)
    op.create_index(op.f('ix_usuarios_telefone'), 'usuarios', ['telefone'], unique=True)

    # Atualizar tabela contratante
    op.add_column('contratante', sa.Column('id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contratante', 'usuarios', ['id'], ['id'])
    op.drop_column('contratante', 'id_contratante')
    op.drop_column('contratante', 'nome')
    op.drop_column('contratante', 'cpf')
    op.drop_column('contratante', 'email')
    op.drop_column('contratante', 'telefone')
    op.drop_column('contratante', 'telefone_emergencia')
    op.drop_column('contratante', 'senha')
    op.drop_column('contratante', 'genero')
    op.drop_column('contratante', 'data_nascimento')

    # Atualizar tabela cuidador
    op.add_column('cuidador', sa.Column('id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cuidador', 'usuarios', ['id'], ['id'])
    op.drop_column('cuidador', 'id_cuidador')
    op.drop_column('cuidador', 'nome')
    op.drop_column('cuidador', 'cpf')
    op.drop_column('cuidador', 'email')
    op.drop_column('cuidador', 'telefone')
    op.drop_column('cuidador', 'senha')
    op.drop_column('cuidador', 'genero')
    op.drop_column('cuidador', 'data_nascimento')

    # Atualizar chaves estrangeiras relacionadas
    op.drop_constraint('endereco_id_contratante_fkey', 'endereco', type_='foreignkey')
    op.create_foreign_key(None, 'endereco', 'contratante', ['id_contratante'], ['id'])

    op.drop_constraint('endereco_cuidador_id_cuidador_fkey', 'endereco_cuidador', type_='foreignkey')
    op.create_foreign_key(None, 'endereco_cuidador', 'cuidador', ['id_cuidador'], ['id'])

    op.drop_constraint('hobbies_id_contratante_fkey', 'hobbies', type_='foreignkey')
    op.create_foreign_key(None, 'hobbies', 'contratante', ['id_contratante'], ['id'])

    op.drop_constraint('hobbies_cuidador_id_cuidador_fkey', 'hobbies_cuidador', type_='foreignkey')
    op.create_foreign_key(None, 'hobbies_cuidador', 'cuidador', ['id_cuidador'], ['id'])

    op.drop_constraint('questionario_id_contratante_fkey', 'questionario', type_='foreignkey')
    op.create_foreign_key(None, 'questionario', 'contratante', ['id_contratante'], ['id'])

    op.drop_constraint('questionario_cuidador_id_cuidador_fkey', 'questionario_cuidador', type_='foreignkey')
    op.create_foreign_key(None, 'questionario_cuidador', 'cuidador', ['id_cuidador'], ['id'])


def downgrade():
    # Reverter as mudanças
    op.drop_constraint(None, 'questionario_cuidador', type_='foreignkey')
    op.create_foreign_key('questionario_cuidador_id_cuidador_fkey', 'questionario_cuidador', 'cuidador', ['id_cuidador'], ['id_cuidador'])

    op.drop_constraint(None, 'questionario', type_='foreignkey')
    op.create_foreign_key('questionario_id_contratante_fkey', 'questionario', 'contratante', ['id_contratante'], ['id_contratante'])

    op.drop_constraint(None, 'hobbies_cuidador', type_='foreignkey')
    op.create_foreign_key('hobbies_cuidador_id_cuidador_fkey', 'hobbies_cuidador', 'cuidador', ['id_cuidador'], ['id_cuidador'])

    op.drop_constraint(None, 'hobbies', type_='foreignkey')
    op.create_foreign_key('hobbies_id_contratante_fkey', 'hobbies', 'contratante', ['id_contratante'], ['id_contratante'])

    op.drop_constraint(None, 'endereco_cuidador', type_='foreignkey')
    op.create_foreign_key('endereco_cuidador_id_cuidador_fkey', 'endereco_cuidador', 'cuidador', ['id_cuidador'], ['id_cuidador'])

    op.drop_constraint(None, 'endereco', type_='foreignkey')
    op.create_foreign_key('endereco_id_contratante_fkey', 'endereco', 'contratante', ['id_contratante'], ['id_contratante'])

    # Reverter tabela cuidador
    op.add_column('cuidador', sa.Column('data_nascimento', sa.Date(), nullable=True))
    op.add_column('cuidador', sa.Column('genero', sa.String(), nullable=True))
    op.add_column('cuidador', sa.Column('senha', sa.String(), nullable=True))
    op.add_column('cuidador', sa.Column('telefone', sa.String(), nullable=True))
    op.add_column('cuidador', sa.Column('email', sa.String(), nullable=True))
    op.add_column('cuidador', sa.Column('cpf', sa.String(length=14), nullable=True))
    op.add_column('cuidador', sa.Column('nome', sa.String(), nullable=True))
    op.add_column('cuidador', sa.Column('id_cuidador', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'cuidador', type_='foreignkey')
    op.drop_column('cuidador', 'id')

    # Reverter tabela contratante
    op.add_column('contratante', sa.Column('data_nascimento', sa.Date(), nullable=True))
    op.add_column('contratante', sa.Column('genero', sa.String(), nullable=True))
    op.add_column('contratante', sa.Column('senha', sa.String(), nullable=True))
    op.add_column('contratante', sa.Column('telefone_emergencia', sa.String(), nullable=True))
    op.add_column('contratante', sa.Column('telefone', sa.String(), nullable=True))
    op.add_column('contratante', sa.Column('email', sa.String(), nullable=True))
    op.add_column('contratante', sa.Column('cpf', sa.String(length=14), nullable=True))
    op.add_column('contratante', sa.Column('nome', sa.String(), nullable=True))
    op.add_column('contratante', sa.Column('id_contratante', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'contratante', type_='foreignkey')
    op.drop_column('contratante', 'id')

    # Remover tabela usuarios
    op.drop_index(op.f('ix_usuarios_telefone'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_email'), table_name='usuarios')
    op.drop_index(op.f('ix_usuarios_cpf'), table_name='usuarios')
    op.drop_table('usuarios') 