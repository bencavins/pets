"""add users

Revision ID: 6637d4253915
Revises: b4e53ab874bf
Create Date: 2024-07-01 10:19:36.912349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6637d4253915'
down_revision = 'b4e53ab874bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
