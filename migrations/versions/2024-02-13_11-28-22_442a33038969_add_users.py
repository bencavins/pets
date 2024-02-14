"""add users

Revision ID: 442a33038969
Revises: 8067f1a2b202
Create Date: 2024-02-13 11:28:22.216198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '442a33038969'
down_revision = '8067f1a2b202'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###