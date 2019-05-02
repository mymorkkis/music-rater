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
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('rating', sa.Integer, nullable=False),
        sa.Column('artist_id', sa.BigInteger, sa.ForeignKey('Artist.id'), nullable=False),
        sa.Column('album_id', sa.BigInteger, sa.ForeignKey('Album.id'), nullable=True),
        sa.Column('track_id', sa.BigInteger, sa.ForeignKey('Track.id'), nullable=True)
    )


def downgrade():
    op.drop_table('music_rating')
