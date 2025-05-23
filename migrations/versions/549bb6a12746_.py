"""empty message

Revision ID: 549bb6a12746
Revises: e4a15b9a9d9f
Create Date: 2025-04-25 18:13:42.062942

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '549bb6a12746'
down_revision = 'e4a15b9a9d9f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Comment', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'Post', ['post_id'], ['id'])

    with op.batch_alter_table('Media', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'Post', ['post_id'], ['id'])

    with op.batch_alter_table('Post', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'User', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('Media', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('Comment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
