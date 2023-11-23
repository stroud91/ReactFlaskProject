"""empty message

Revision ID: 63bd349e2e48
Revises: ffdc0a98111c
Create Date: 2023-10-01 20:15:58.202553

"""
from alembic import op
import sqlalchemy as sa



revision = '63bd349e2e48'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('business_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=True)




def downgrade():

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.alter_column('updated_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('created_at',
               existing_type=sa.DATETIME(),
               nullable=False)
        batch_op.alter_column('business_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)


