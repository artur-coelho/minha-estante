"""init

Revision ID: 016061df6dd7
Revises: 
Create Date: 2022-06-23 00:43:35.657070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '016061df6dd7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'usuario',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('senha', sa.String(50), nullable=False),
    )

def downgrade():
    op.drop_table('usuario')