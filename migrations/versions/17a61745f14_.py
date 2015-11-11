"""empty message

Revision ID: 17a61745f14
Revises: 54cf585c2c7
Create Date: 2015-11-09 11:37:52.579904

"""

# revision identifiers, used by Alembic.
revision = '17a61745f14'
down_revision = '54cf585c2c7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###