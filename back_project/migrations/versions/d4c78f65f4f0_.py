"""empty message

Revision ID: d4c78f65f4f0
Revises: c98195e5931b
Create Date: 2021-10-31 18:13:07.271370

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd4c78f65f4f0'
down_revision = 'c98195e5931b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('access', 'longitude')
    op.drop_column('access', 'latitude')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('access', sa.Column('latitude', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('access', sa.Column('longitude', mysql.VARCHAR(length=255), nullable=True))
    # ### end Alembic commands ###