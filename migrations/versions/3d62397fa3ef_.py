"""empty message

Revision ID: 3d62397fa3ef
Revises: 7ba35fe795c7
Create Date: 2024-01-22 23:44:32.213769

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d62397fa3ef'
down_revision = '7ba35fe795c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=True),
    sa.Column('end_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['photo_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('events')
    # ### end Alembic commands ###