"""empty message

Revision ID: 17d2ede29cab
Revises: 499e7864de12
Create Date: 2020-06-04 12:04:44.057804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '17d2ede29cab'
down_revision = '499e7864de12'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_work_iswc', table_name='work')
    op.create_index(op.f('ix_work_iswc'), 'work', ['iswc'], unique=False)
    op.add_column('work_provider', sa.Column('provider_reference', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('work_provider', 'provider_reference')
    op.drop_index(op.f('ix_work_iswc'), table_name='work')
    op.create_index('ix_work_iswc', 'work', ['iswc'], unique=True)
    # ### end Alembic commands ###