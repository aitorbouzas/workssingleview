"""empty message

Revision ID: 499e7864de12
Revises: 
Create Date: 2020-06-03 16:26:07.859254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '499e7864de12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('deleted_timestamp', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('work',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('deleted_timestamp', sa.DateTime(), nullable=True),
    sa.Column('iswc', sa.String(length=32), nullable=True),
    sa.Column('title', sa.String(length=128), nullable=True),
    sa.Column('contributors', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_work_iswc'), 'work', ['iswc'], unique=True)
    op.create_table('work_provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_timestamp', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('deleted_timestamp', sa.DateTime(), nullable=True),
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('work_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], ),
    sa.ForeignKeyConstraint(['work_id'], ['work.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_work_provider_provider_id'), 'work_provider', ['provider_id'], unique=False)
    op.create_index(op.f('ix_work_provider_work_id'), 'work_provider', ['work_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_work_provider_work_id'), table_name='work_provider')
    op.drop_index(op.f('ix_work_provider_provider_id'), table_name='work_provider')
    op.drop_table('work_provider')
    op.drop_index(op.f('ix_work_iswc'), table_name='work')
    op.drop_table('work')
    op.drop_table('provider')
    # ### end Alembic commands ###