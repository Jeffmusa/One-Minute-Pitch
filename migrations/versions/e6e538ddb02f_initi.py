"""Initi

Revision ID: e6e538ddb02f
Revises: b42baed35b5b
Create Date: 2018-06-27 16:44:36.591363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6e538ddb02f'
down_revision = 'b42baed35b5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('like', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###
