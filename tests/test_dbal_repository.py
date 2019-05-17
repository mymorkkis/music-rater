import pytest
from sqlalchemy.orm.exc import NoResultFound

from src.dbal.dbal_repository import DBALRepository
from src.dbal.models.artist import Artist
from src.dbal.models.genre import Genre


@pytest.fixture
def dbal_repository(test_session):
    genre_repository = DBALRepository(model=Genre, db_session=test_session)

    yield genre_repository

    genre_repository.drop_table()


@pytest.fixture
def stored_genre(dbal_repository):
    genre = Genre(name='Rock')
    stored_genre = dbal_repository.add(genre)
    return stored_genre


class TestDBALRepsoitory:

    def test_can_add_an_entity(self, stored_genre):
        assert stored_genre.id is not None
        assert stored_genre.name == 'Rock'

    def test_can_get_an_entity_by_id(self, stored_genre, dbal_repository):
        genre = dbal_repository.get_by_id(entity_id=stored_genre.id)
        assert genre == stored_genre

    def test_fetching_a_non_existent_entity_raises_no_result_found(self, dbal_repository):
        with pytest.raises(NoResultFound):
            dbal_repository.get_by_id(entity_id=999)

    def test_can_find_an_entity_by_attribute(self, stored_genre, dbal_repository):
        genres = dbal_repository.find(attribute='name', value='Rock')
        assert genres[0].id == stored_genre.id

    def test_can_find_multiple_entities_by_attribute(self, test_session):
        dbal_repository = DBALRepository(model=Artist, db_session=test_session)
        blur = dbal_repository.add(Artist(name='Blur', artist_type='group', genre_id=1))
        oasis = dbal_repository.add(Artist(name='Oasis', artist_type='group', genre_id=1))
        genres = dbal_repository.find(attribute='artist_type', value='group')

        assert set(genres) == {blur, oasis}

        dbal_repository.drop_table()

    def test_empty_list_returned_if_no_entities_found(self, dbal_repository):
        genres = dbal_repository.find(attribute='name', value='Non Existing')
        assert genres == []

    def test_attribute_error_raised_if_unknown_attrubute_passed_in_to_find(self, dbal_repository):
        with pytest.raises(AttributeError):
            dbal_repository.find(attribute='boom', value='BOOM')

    def test_can_delete_an_entity(self, stored_genre, dbal_repository):
        dbal_repository.delete(stored_genre)
        with pytest.raises(NoResultFound):
            dbal_repository.get_by_id(entity_id=stored_genre.id)

    def test_attempt_to_delete_a_non_existent_entity_does_not_raise_error(self, dbal_repository):
        genre = Genre(name='Not Stored')
        dbal_repository.delete(genre)

    def test_can_update_an_entity(self, stored_genre, dbal_repository):
        stored_genre.name = 'Punk'
        updated_genre = dbal_repository.update(stored_genre)
        stored_updated_genre = dbal_repository.get_by_id(entity_id=updated_genre.id)
        assert updated_genre.name == 'Punk'
        assert stored_updated_genre.name == 'Punk'
        assert stored_updated_genre.id == stored_genre.id

    def test_upsert_creates_an_entity_if_none_found(self, dbal_repository):
        new_genre = Genre(name='Dance')
        stored_genre = dbal_repository.upsert(new_genre)
        assert stored_genre.id is not None
        assert stored_genre.name == 'Dance'

    def test_upsert_updates_an_entity_if_found(self, stored_genre, dbal_repository):
        assert stored_genre.name == 'Rock'
        stored_genre.name = 'Punk'
        updated_entity = dbal_repository.upsert(stored_genre)
        stored_updated_entity = dbal_repository.get_by_id(entity_id=updated_entity.id)
        assert updated_entity.name == 'Punk'
        assert stored_updated_entity.name == 'Punk'
        assert stored_updated_entity.id
