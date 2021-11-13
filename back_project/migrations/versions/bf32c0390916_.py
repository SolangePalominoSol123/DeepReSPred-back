"""empty message

Revision ID: bf32c0390916
Revises: 1bbd5e160b5f
Create Date: 2021-11-08 13:26:46.424879

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bf32c0390916'
down_revision = '1bbd5e160b5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('filexreq_ibfk_1', 'filexreq', type_='foreignkey')
    op.drop_constraint('filexreq_ibfk_2', 'filexreq', type_='foreignkey')
    op.drop_column('filexreq', 'idRequest')
    op.drop_column('filexreq', 'idFile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('filexreq', sa.Column('idFile', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('filexreq', sa.Column('idRequest', mysql.VARCHAR(length=8), nullable=True))
    op.create_foreign_key('filexreq_ibfk_2', 'filexreq', 'request', ['idRequest'], ['idRequest'])
    op.create_foreign_key('filexreq_ibfk_1', 'filexreq', 'file', ['idFile'], ['idFile'])
    # ### end Alembic commands ###
