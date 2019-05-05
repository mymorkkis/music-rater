"""create tables: artist, album, track, music_rating

Revision ID: f9d708416d19
Revises:
Create Date: 2019-05-05 15:47:51.844759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9d708416d19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_genre'))
    )
    op.create_index(op.f('ix_genre_name'), 'genre', ['name'], unique=False)
    op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('artist_type', sa.String(length=5), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.CheckConstraint('artist_type IN ("solo", "group")', name=op.f('ck_artist_artist_type_check')),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name=op.f('fk_artist_genre_id_genre')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_artist')),
    sa.UniqueConstraint('name', 'genre_id', 'artist_type', name=op.f('uq_artist_name_genre_id_artist_type'))
    )
    op.create_index(op.f('ix_artist_name'), 'artist', ['name'], unique=False)
    op.create_table('album',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name=op.f('fk_album_artist_id_artist')),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name=op.f('fk_album_genre_id_genre')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_album')),
    sa.UniqueConstraint('name', 'artist_id', name=op.f('uq_album_name_artist_id'))
    )
    op.create_index(op.f('ix_album_name'), 'album', ['name'], unique=False)
    op.create_table('track',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], name=op.f('fk_track_album_id_album')),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name=op.f('fk_track_artist_id_artist')),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name=op.f('fk_track_genre_id_genre')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_track')),
    sa.UniqueConstraint('name', 'album_id', name=op.f('uq_track_name_album_id')),
    sa.UniqueConstraint('name', 'artist_id', name=op.f('uq_track_name_artist_id'))
    )
    op.create_index(op.f('ix_track_name'), 'track', ['name'], unique=False)
    op.create_table('music_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True, onupdate=sa.func.current_timestamp()),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['album.id'], name=op.f('fk_music_rating_album_id_album')),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name=op.f('fk_music_rating_artist_id_artist')),
    sa.ForeignKeyConstraint(['track_id'], ['track.id'], name=op.f('fk_music_rating_track_id_track')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_music_rating'))
    )


def downgrade():
    op.drop_table('music_rating')
    op.drop_index(op.f('ix_track_name'), table_name='track')
    op.drop_table('track')
    op.drop_index(op.f('ix_album_name'), table_name='album')
    op.drop_table('album')
    op.drop_index(op.f('ix_artist_name'), table_name='artist')
    op.drop_table('artist')
    op.drop_index(op.f('ix_genre_name'), table_name='genre')
    op.drop_table('genre')
