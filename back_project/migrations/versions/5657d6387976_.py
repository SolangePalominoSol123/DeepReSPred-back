"""empty message

Revision ID: 5657d6387976
Revises: 25c694255874
Create Date: 2021-10-31 19:41:21.330935

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5657d6387976'
down_revision = '25c694255874'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('request_ibfk_2', 'request', type_='foreignkey')
    op.drop_column('request', 'longitude')
    op.drop_column('request', 'latitude')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('latitude', mysql.VARCHAR(length=255), nullable=True))
    op.add_column('request', sa.Column('longitude', mysql.VARCHAR(length=255), nullable=True))
    op.create_foreign_key('request_ibfk_2', 'request', 'endpoint', ['latitude'], ['latitude'])
    # ### end Alembic commands ###