"""n

Revision ID: 5465512fd895
Revises: 7bc6c08c6fbd
Create Date: 2018-06-28 09:12:58.519055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5465512fd895'
down_revision = '7bc6c08c6fbd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('likes_promotion_id_fkey', 'likes', type_='foreignkey')
    op.drop_constraint('likes_pick_id_fkey', 'likes', type_='foreignkey')
    op.drop_constraint('likes_interview_id_fkey', 'likes', type_='foreignkey')
    op.drop_column('likes', 'promotion_id')
    op.drop_column('likes', 'pick_id')
    op.drop_column('likes', 'interview_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('likes', sa.Column('interview_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('likes', sa.Column('pick_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('likes', sa.Column('promotion_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('likes_interview_id_fkey', 'likes', 'interview', ['interview_id'], ['id'])
    op.create_foreign_key('likes_pick_id_fkey', 'likes', 'pick', ['pick_id'], ['id'])
    op.create_foreign_key('likes_promotion_id_fkey', 'likes', 'promotion', ['promotion_id'], ['id'])
    # ### end Alembic commands ###
