"""empty message

Revision ID: 7bd4346fbc
Revises: 456a945560f6
Create Date: 2015-11-05 11:26:22.375184

"""

# revision identifiers, used by Alembic.
revision = '7bd4346fbc'
down_revision = '456a945560f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    ### end Alembic commands ###