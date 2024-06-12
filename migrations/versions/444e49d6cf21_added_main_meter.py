"""added main meter

Revision ID: 444e49d6cf21
Revises: 00a4d048ccb0
Create Date: 2024-06-12 11:47:34.973479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '444e49d6cf21'
down_revision = '00a4d048ccb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meter', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_main_meter', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('main_meter_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'meter', ['main_meter_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('meter', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('main_meter_id')
        batch_op.drop_column('is_main_meter')

    # ### end Alembic commands ###
