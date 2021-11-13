"""empty message

Revision ID: b897da7918c1
Revises: bf32c0390916
Create Date: 2021-11-08 13:27:35.742226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b897da7918c1'
down_revision = 'bf32c0390916'
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
