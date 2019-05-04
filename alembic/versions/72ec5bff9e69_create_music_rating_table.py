"""create music rating table

Revision ID: 72ec5bff9e69
Revises: e3bf223c7822
Create Date: 2019-05-02 19:00:31.670404

"""
import sqlalchemy as sa
from alembic import op


revision = '72ec5bff9e69'
down_revision = 'e3bf223c7822'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'music_rating',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, server_default=sa.func.current_timestamp()),
        sa.Column('updated_at', sa.DateTime, nullable=True, onupdate=sa.func.current_timestamp()),
        sa.Column('artist_id', sa.Integer, sa.ForeignKey('artist.id'), nullable=False),
        sa.Column('album_id', sa.Integer, sa.ForeignKey('album.id'), nullable=True),
        sa.Column('track_id', sa.Integer, sa.ForeignKey('track.id'), nullable=True)
    )


def downgrade():
    op.drop_table('music_rating')
