"""create artist table

Revision ID: 5118d9c04682
Revises:
Create Date: 2019-04-28 09:40:23.696470

"""
import sqlalchemy as sa
from alembic import op


revision = '5118d9c04682'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'artist',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('artist_type', sa.Enum('solo', 'group'), nullable=False),
    )


def downgrade():
    op.drop_table('artist')
