"""add user table

Revision ID: 0de2ff9b2eff
Revises: 90091cba8881
Create Date: 2023-02-12 19:44:05.304978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0de2ff9b2eff'
down_revision = '90091cba8881'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
