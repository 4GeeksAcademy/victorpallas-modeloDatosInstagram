"""empty message

Revision ID: e4a15b9a9d9f
Revises: a610ca0c4b11
Create Date: 2025-04-25 18:10:21.859587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a15b9a9d9f'
down_revision = 'a610ca0c4b11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Follower', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'User', ['user_to_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Follower', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
