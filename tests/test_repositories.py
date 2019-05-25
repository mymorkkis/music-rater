import pytest

from src.dbal import encode_id
from src.dbal.models.genre import DBALGenre
from src.dbal.repositories.dbal_repository import NotFound
from src.dbal.repositories.genre_repository import GenreRepository
from src.domain.entities.artist import Artist
from src.domain.entities.album import Album
from src.domain.entities.genre import Genre


@pytest.fixture
def genre_entity(genre_repository):
    return genre_repository.add(Genre(name='Rock'))


@pytest.fixture
def artist_entity(artist_repository, genre_entity):
    return artist_repository.add(Artist(name='Blur', type_='group', genre_id=genre_entity.entity_id))


@pytest.fixture
def album_entity(album_repository, artist_entity, genre_entity):
    return album_repository.add(Album(name='Blur', artist_id=artist_entity.entity_id, genre_id=genre_entity.entity_id))


def test_can_add_and_fetch_genre_entity(genre_repository, genre_entity):
    stored_genre = genre_repository.get_by_id(genre_entity.entity_id)
    assert stored_genre
    assert stored_genre.entity_id == genre_entity.entity_id
    assert stored_genre.name == genre_entity.name


def test_can_add_and_fetch_artist_entity(artist_repository, artist_entity):
    stored_artist = artist_repository.get_by_id(artist_entity.entity_id)
    assert stored_artist
    assert stored_artist.entity_id == artist_entity.entity_id
    assert stored_artist.name == artist_entity.name
    assert stored_artist.type_ == artist_entity.type_
    assert stored_artist.genre_id == artist_entity.genre_id


def test_can_add_and_fetch_album_entity(album_repository, album_entity):
    stored_album = album_repository.get_by_id(album_entity.entity_id)
    assert stored_album
    assert stored_album.entity_id == album_entity.entity_id
    assert stored_album.name == album_entity.name
    assert stored_album.artist_id == album_entity.artist_id
    assert stored_album.genre_id == album_entity.genre_id
