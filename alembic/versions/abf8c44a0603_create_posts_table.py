"""create posts table

Revision ID: abf8c44a0603
Revises: 42b7a742bfd1
Create Date: 2023-02-12 19:29:12.351795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abf8c44a0603'
down_revision = '42b7a742bfd1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
    sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass