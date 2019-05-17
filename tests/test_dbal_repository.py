import pytest
from sqlalchemy.orm.exc import NoResultFound

from src.dbal.dbal_repository import DBALRepository
from src.dbal.models.genre import Genre


@pytest.fixture
def dbal_repository(test_session):
    return DBALRepository(model=Genre, db_session=test_session)


@pytest.fixture
def stored_genre(dbal_repository):
    genre = Genre(name='Rock')
    stored_genre = dbal_repository.add(genre)
    return stored_genre


class TestDBALRepsoitory:

    def test_can_add_an_entity(self, stored_genre):
        assert stored_genre.id is not None
        assert stored_genre.name == 'Rock'

    def test_can_get_an_entity(self, stored_genre, dbal_repository):
        genre = dbal_repository.get(entity_id=stored_genre.id)
        assert genre == stored_genre

    def test_fetching_a_non_existent_entity_raises_no_result_found(self, dbal_repository):
        with pytest.raises(NoResultFound):
            dbal_repository.get(entity_id=999)

    def test_can_delete_an_entity(self, stored_genre, dbal_repository):
        dbal_repository.delete(stored_genre)
        with pytest.raises(NoResultFound):
            dbal_repository.get(entity_id=stored_genre.id)

    def test_can_update_an_entity(self, stored_genre, dbal_repository):
        stored_genre.name = 'Punk'
        updated_genre = dbal_repository.update(stored_genre)
        stored_updated_genre = dbal_repository.get(entity_id=updated_genre.id)
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
        stored_updated_entity = dbal_repository.get(entity_id=updated_entity.id)
        assert updated_entity.name == 'Punk'
        assert stored_updated_entity.name == 'Punk'
        assert stored_updated_entity.id
