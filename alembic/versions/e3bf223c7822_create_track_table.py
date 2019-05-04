"""create track table

Revision ID: e3bf223c7822
Revises: b0795434405c
Create Date: 2019-04-28 10:12:13.115227

"""
import sqlalchemy as sa
from alembic import op


revision = 'e3bf223c7822'
down_revision = 'b0795434405c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'track',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('artist_id', sa.Integer, sa.ForeignKey('artist.id'), nullable=False),
        sa.Column('album_id', sa.Integer, sa.ForeignKey('album.id'), nullable=True),
    )

def downgrade():
    op.drop_table('track')
