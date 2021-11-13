"""empty message

Revision ID: c0f6547b99d6
Revises: f67382334567
Create Date: 2021-10-31 13:16:35.913577

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c0f6547b99d6'
down_revision = 'f67382334567'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('access_ibfk_1', 'access', type_='foreignkey')
    op.drop_column('access', 'idRequest')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('access', sa.Column('idRequest', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('access_ibfk_1', 'access', 'request', ['idRequest'], ['idRequest'])
    # ### end Alembic commands ###
