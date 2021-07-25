"""empty message

Revision ID: 51c55426241d
Revises: 
Create Date: 2021-07-21 22:56:50.892313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51c55426241d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('userid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('userpassword', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.Column('registdatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('userid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
