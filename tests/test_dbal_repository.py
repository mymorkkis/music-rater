import pytest
from sqlalchemy.orm.exc import NoResultFound

from src.dbal.dbal_repository import DBALRepository
from src.dbal.models.artist import Artist
from src.dbal.models.genre import Genre


@pytest.fixture
def genre_repository(test_session):
    return DBALRepository(model=Genre, db_session=test_session)


@pytest.fixture
def stored_genre(genre_repository):
    genre = Genre(name='Rock')
    stored_genre = genre_repository.add(genre)
    return stored_genre


class TestDBALRepsoitory:

    def test_can_add_an_entity(self, stored_genre):
        assert stored_genre.id is not None
        assert stored_genre.name == 'Rock'

    def test_can_get_an_entity_by_id(self, stored_genre, genre_repository):
        genre = genre_repository.get_by_id(entity_id=stored_genre.id)
        assert genre == stored_genre

    def test_fetching_a_non_existent_entity_raises_no_result_found(self, genre_repository):
        with pytest.raises(NoResultFound):
            genre_repository.get_by_id(entity_id=999)

    def test_can_find_an_entity_by_attribute(self, stored_genre, genre_repository):
        genres = genre_repository.find(attribute='name', value='Rock')
        assert genres[0].id == stored_genre.id

    def test_can_find_multiple_entities_by_attribute(self, test_session):
        artist_repository = DBALRepository(model=Artist, db_session=test_session)
        blur = artist_repository.add(Artist(name='Blur', artist_type='group', genre_id=1))
        oasis = artist_repository.add(Artist(name='Oasis', artist_type='group', genre_id=1))
        genres = artist_repository.find(attribute='artist_type', value='group')

        assert set(genres) == {blur, oasis}

    def test_empty_list_returned_if_no_entities_found(self, genre_repository):
        genres = genre_repository.find(attribute='name', value='Non Existing')
        assert genres == []

    def test_attribute_error_raised_if_unknown_attrubute_passed_in_to_find(self, genre_repository):
        with pytest.raises(AttributeError):
            genre_repository.find(attribute='boom', value='BOOM')

    def test_can_delete_an_entity(self, stored_genre, genre_repository):
        genre_repository.delete(stored_genre)
        with pytest.raises(NoResultFound):
            genre_repository.get_by_id(entity_id=stored_genre.id)

    def test_attempt_to_delete_a_non_existent_entity_does_not_raise_error(self, genre_repository):
        genre = Genre(name='Not Stored')
        genre_repository.delete(genre)

    def test_can_update_an_entity(self, stored_genre, genre_repository):
        stored_genre.name = 'Punk'
        updated_genre = genre_repository.update(stored_genre)
        stored_updated_genre = genre_repository.get_by_id(entity_id=updated_genre.id)
        assert updated_genre.name == 'Punk'
        assert stored_updated_genre.name == 'Punk'
        assert stored_updated_genre.id == stored_genre.id

    def test_upsert_creates_an_entity_if_none_found(self, genre_repository):
        new_genre = Genre(name='Dance')
        stored_genre = genre_repository.upsert(new_genre)
        assert stored_genre.id is not None
        assert stored_genre.name == 'Dance'

    def test_upsert_updates_an_entity_if_found(self, stored_genre, genre_repository):
        assert stored_genre.name == 'Rock'
        stored_genre.name = 'Punk'
        updated_entity = genre_repository.upsert(stored_genre)
        stored_updated_entity = genre_repository.get_by_id(entity_id=updated_entity.id)
        assert updated_entity.name == 'Punk'
        assert stored_updated_entity.name == 'Punk'
        assert stored_updated_entity.id

    def test_can_truncate_table(self, stored_genre, genre_repository):
        genre_rows = genre_repository.session.query(genre_repository.model)
        assert len(genre_rows.all()) == 1
        genre_repository.truncate_table()
        assert len(genre_rows.all()) == 0
