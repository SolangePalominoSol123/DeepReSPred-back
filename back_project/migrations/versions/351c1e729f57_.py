"""empty message

Revision ID: 351c1e729f57
Revises: 2b5aed8c4ce0
Create Date: 2021-11-02 01:10:25.154154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '351c1e729f57'
down_revision = '2b5aed8c4ce0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('access',
    sa.Column('idAccess', sa.Integer(), nullable=False),
    sa.Column('ipClient', sa.String(length=15), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('idEndpoint', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['idEndpoint'], ['endpoint.idEndpoint'], ),
    sa.PrimaryKeyConstraint('idAccess')
    )
    op.add_column('request', sa.Column('idAccess', sa.Integer(), nullable=True))
    op.drop_constraint('request_ibfk_2', 'request', type_='foreignkey')
    op.create_foreign_key(None, 'request', 'access', ['idAccess'], ['idAccess'])
    op.drop_column('request', 'ipClient')
    op.drop_column('request', 'idEndpoint')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('request', sa.Column('idEndpoint', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('request', sa.Column('ipClient', mysql.VARCHAR(length=15), nullable=True))
    op.drop_constraint(None, 'request', type_='foreignkey')
    op.create_foreign_key('request_ibfk_2', 'request', 'endpoint', ['idEndpoint'], ['idEndpoint'])
    op.drop_column('request', 'idAccess')
    op.drop_table('access')
    # ### end Alembic commands ###
