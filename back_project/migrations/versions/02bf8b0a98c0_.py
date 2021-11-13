"""empty message

Revision ID: 02bf8b0a98c0
Revises: e8f563f8cadb
Create Date: 2021-10-31 18:55:26.914755

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '02bf8b0a98c0'
down_revision = 'e8f563f8cadb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('endpoint', sa.Column('idEndpoint', sa.Integer(), nullable=False))
    op.alter_column('endpoint', 'latitude',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('endpoint', 'longitude',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.drop_column('endpoint', 'ipClient')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('endpoint', sa.Column('ipClient', mysql.VARCHAR(length=15), nullable=True))
    op.alter_column('endpoint', 'longitude',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('endpoint', 'latitude',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.drop_column('endpoint', 'idEndpoint')
    # ### end Alembic commands ###