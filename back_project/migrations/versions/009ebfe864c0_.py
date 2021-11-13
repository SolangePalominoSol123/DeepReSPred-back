"""empty message

Revision ID: 009ebfe864c0
Revises: 11c21fa93728
Create Date: 2021-11-08 13:05:09.506905

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '009ebfe864c0'
down_revision = '11c21fa93728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    print("roroodod")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('filexreq', 'idFile',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('filexreq', 'idRequest',
               existing_type=mysql.VARCHAR(length=8),
               nullable=False)
    op.drop_column('filexreq', 'idFilexreq')
    op.alter_column('file', 'isFragment',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    op.alter_column('file', 'haveStructure',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'0'"))
    # ### end Alembic commands ###