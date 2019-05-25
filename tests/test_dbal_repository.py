import pytest
from sqlalchemy.orm.exc import NoResultFound

from src.dbal import encode_id
from src.dbal.models.artist import DBALArtist
from src.dbal.models.genre import DBALGenre
from src.dbal.repositories.dbal_repository import NotFound

from src.domain.entities.artist import Artist
from src.domain.entities.genre import Genre


@pytest.fixture
def genre_entity():
    return Genre(
        entity_id=encode_id.genre(1),
        name='Rock',
    )


class TestDBALRepsoitory:

    def test_can_add_and_fetch_dbal_entity_by_id(self, genre_repository, genre_entity):
        genre_repository.add(genre_entity)
        stored_dbal_entity = genre_repository.get_by_id(genre_entity.entity_id)
        assert stored_dbal_entity
        assert stored_dbal_entity.entity_id == genre_entity.entity_id
        assert stored_dbal_entity.name == genre_entity.name

    def test_can_find_domain_entity_by_attribute(self, genre_repository, genre_entity):
        genre_repository.add(genre_entity)
        found_entity = genre_repository.find(name='Rock')[0]
        assert found_entity.entity_id == genre_entity.entity_id
        assert found_entity.name == genre_entity.name

    def test_can_find_multiple_entities_by_attribute(self, artist_repository, genre_entity):
        blur = artist_repository.add(Artist( name='Blur', type_='group', genre_id=genre_entity.entity_id))
        oasis = artist_repository.add(Artist( name='Oasis', type_='group', genre_id=genre_entity.entity_id))
        found_artists = artist_repository.find(artist_type='group')
        found_artist_names = {artist.name for artist in found_artists}
        assert found_artist_names == {'Blur', 'Oasis'}

    def test_can_find_entity_by_multiple_attributes(self, artist_repository, genre_entity):
        blur_group = artist_repository.add(Artist(name='Blur', type_='group', genre_id=genre_entity.entity_id))
        blur_solo = artist_repository.add(Artist(name='Blur', type_='solo', genre_id=genre_entity.entity_id))
        found_artists = artist_repository.find(name='Blur', artist_type='group')
        assert found_artists == [blur_group]

    def test_can_delete_genre_dbal_entity(self, genre_repository, genre_entity):
        genre_repository.add(genre_entity)
        assert genre_repository.get_by_id(genre_entity.entity_id)
        genre_repository.delete(genre_entity)
        with pytest.raises(NotFound) as err:
            assert genre_repository.get_by_id(genre_entity.entity_id)
            assert err.message == 'Entity: genre could not be found'

    def test_can_update_genre_dbal_entity(self, genre_repository, genre_entity):
        genre_repository.add(genre_entity)
        genre_entity.name = 'Blues'
        updated_entity = genre_repository.update(genre_entity)
        dbal_entity = genre_repository.get_by_id(genre_entity.entity_id)
        assert dbal_entity.name == updated_entity.name == 'Blues'

    def test_empty_list_returned_if_no_entities_found(self, genre_repository):
        genres = genre_repository.find(name='Non Existing')
        assert genres == []

    def test_attribute_error_raised_if_unknown_attrubute_passed_in_to_find(self, genre_repository):
        with pytest.raises(AttributeError):
            genre_repository.find(boom='BOOM')

    def test_upsert_creates_an_entity_if_none_found(self, genre_repository, genre_entity):
        genre_repository.upsert(genre_entity)
        stored_entity = genre_repository.get_by_id(genre_entity.entity_id)
        assert stored_entity

    def test_upsert_updates_an_entity_if_found(self, genre_repository, genre_entity):
        assert genre_entity.name == 'Rock'
        genre_entity.name = 'Punk'
        genre_repository.upsert(genre_entity)
        rock_genre = genre_repository.find(name='Rock')
        assert not rock_genre
        punk_genre = genre_repository.find(name='Punk')
        assert punk_genre

    def test_can_truncate_table(self, genre_repository, genre_entity):
        genre_repository.add(genre_entity)
        genre_rows = genre_repository.session.query(genre_repository.model)
        assert len(genre_rows.all()) == 1
        genre_repository.truncate_table()
        assert len(genre_rows.all()) == 0
