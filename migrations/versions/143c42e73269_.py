"""empty message

Revision ID: 143c42e73269
Revises: None
Create Date: 2015-09-21 17:24:44.589751

"""

# revision identifiers, used by Alembic.
revision = '143c42e73269'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    ### end Alembic commands ###
