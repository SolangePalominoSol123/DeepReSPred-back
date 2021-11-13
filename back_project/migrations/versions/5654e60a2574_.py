"""empty message

Revision ID: 5654e60a2574
Revises: d8dfae91ce18
Create Date: 2021-11-08 15:26:42.828390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5654e60a2574'
down_revision = 'd8dfae91ce18'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('filexreq', sa.Column('idRequest', sa.String(length=8), nullable=True))
    op.add_column('filexreq', sa.Column('idFile', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'filexreq', 'request', ['idRequest'], ['idRequest'])
    op.create_foreign_key(None, 'filexreq', 'file', ['idFile'], ['idFile'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'filexreq', type_='foreignkey')
    op.drop_constraint(None, 'filexreq', type_='foreignkey')
    op.drop_column('filexreq', 'idFile')
    op.drop_column('filexreq', 'idRequest')
    # ### end Alembic commands ###