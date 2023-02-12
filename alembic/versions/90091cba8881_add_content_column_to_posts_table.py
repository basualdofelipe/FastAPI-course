"""add content column to posts table

Revision ID: 90091cba8881
Revises: abf8c44a0603
Create Date: 2023-02-12 19:38:41.203953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90091cba8881'
down_revision = 'abf8c44a0603'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
