"""empty message

Revision ID: 11c21fa93728
Revises: 87a405926aeb
Create Date: 2021-11-05 21:51:31.536674

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11c21fa93728'
down_revision = '87a405926aeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('nameFile', sa.String(length=255), nullable=True))
    op.drop_column('file', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file', sa.Column('content', sa.BLOB(), nullable=True))
    op.drop_column('file', 'nameFile')
    # ### end Alembic commands ###