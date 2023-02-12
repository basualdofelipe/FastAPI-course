"""add foreign-key to posts table

Revision ID: 610dab029448
Revises: 0de2ff9b2eff
Create Date: 2023-02-12 19:50:18.910048

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '610dab029448'
down_revision = '0de2ff9b2eff'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constrain('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
