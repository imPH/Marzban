"""inbounds table & excluded_inbounds

Revision ID: e91236993f1a
Revises: 671621870b02
Create Date: 2023-02-05 23:21:27.828558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91236993f1a'
down_revision = '671621870b02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('inbounds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inbounds_tag'), 'inbounds', ['tag'], unique=True)
    op.create_table('exclude_inbounds_association',
    sa.Column('proxy_id', sa.Integer(), nullable=True),
    sa.Column('inbound_tag', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['inbound_tag'], ['inbounds.tag'], ),
    sa.ForeignKeyConstraint(['proxy_id'], ['proxies.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('exclude_inbounds_association')
    op.drop_index(op.f('ix_inbounds_tag'), table_name='inbounds')
    op.drop_table('inbounds')
    # ### end Alembic commands ###
