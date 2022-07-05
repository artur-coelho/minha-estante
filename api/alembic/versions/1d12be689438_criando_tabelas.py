"""criando_tabelas

Revision ID: 1d12be689438
Revises: 016061df6dd7
Create Date: 2022-06-23 00:50:19.907135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d12be689438'
down_revision = '016061df6dd7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'livro',
        sa.Column('isbn', sa.Integer, primary_key=True),
        sa.Column('usuario_id', sa.Integer, nullable=False),
        sa.Column('estante_id', sa.Integer, nullable=False),
        sa.Column('edicao', sa.String(50), nullable=False),
        sa.Column('editora', sa.String(50), nullable=False),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('descricao', sa.String(50), nullable=False),
        sa.Column('tipo_capa', sa.String(50), nullable=False),
        sa.Column('genero', sa.String(50), nullable=False),
        sa.Column("data_cadastro", sa.TIMESTAMP(timezone=True), nullable=True),


    )
    op.create_table(
            'estante',
            sa.Column('estante', sa.Integer, primary_key=True),
            sa.Column('nome', sa.String(50), nullable=False),
            sa.Column('num_prateleira', sa.Integer, nullable=False),
           
        )
    op.create_table(
                'metas',
                sa.Column('id_metas', sa.Integer, primary_key=True),
                sa.Column("data_inicial", sa.TIMESTAMP(timezone=True), nullable=True),
                sa.Column("data_final", sa.TIMESTAMP(timezone=True), nullable=True),
                sa.Column('quantidade_leitura', sa.Integer, nullable=False),
                sa.Column('id_metas', sa.Integer, primary_key=True),
                sa.Column('id_metas', sa.Integer, primary_key=True),
                sa.Column('nome', sa.Integer, primary_key=True),
                
            )
    op.create_table(
                    'emprestimo',
                    sa.Column('id_emprestimo', sa.Integer, primary_key=True),
                    sa.Column('nome', sa.String(50), nullable=False),
                    sa.Column('livro_isbn', sa.Integer, nullable=False),
                    sa.Column('livro_usario', sa.Integer, primary_key=True),
                    sa.Column('livro_estante', sa.Integer, primary_key=True),
                    sa.Column('nome', sa.Integer, primary_key=True),
                    sa.ForeignKeyConstraint(
                        ["livro_isbn"],
                        ["livro.isbn"],
            ),
                )
    
def downgrade():
    op.drop_table('livro')
    op.drop_table('estante')
    op.drop_table('metas')
    op.drop_table('emprestimo')