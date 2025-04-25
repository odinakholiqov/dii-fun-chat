"""add_post_table

Revision ID: 5373dfb6b700
Revises: 726f4d3da3a1
Create Date: 2025-04-25 13:32:16.503721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5373dfb6b700'
down_revision = '726f4d3da3a1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('post',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('body', sa.String(length=140), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_user_id'), ['user_id'], unique=False)


def downgrade():
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_user_id'))
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))

    op.drop_table('post')
