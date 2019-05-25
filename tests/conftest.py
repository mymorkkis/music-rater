from pathlib import Path

from alembic.command import downgrade, upgrade
from alembic.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound
import pytest

from src.dbal.repositories.dbal_repository import DBALRepository
from src.dbal.repositories.artist_repository import ArtistRepository
from src.dbal.repositories.album_repository import AlbumRepository
from src.dbal.repositories.genre_repository import GenreRepository
# from src.dbal.repositories.music_rating_repository import MusicRatingRepository
# from src.dbal.repositories.track_repository import TrackRepository


Session = sessionmaker()


TEST_DB = 'test.db'
TEST_DB_PATH = Path.cwd() / TEST_DB
TEST_DATABASE_URI = f'sqlite:///{TEST_DB_PATH}'
ALEMBIC_CONFIG = Path.cwd() / 'alembic.ini'


def apply_migrations():
    '''Applies all alembic migrations for testing session'''
    config = Config(ALEMBIC_CONFIG)
    config.set_main_option('sqlalchemy.url', TEST_DATABASE_URI)
    upgrade(config, 'head')


def downgrade_migrations():
    '''Downgrades all alembic migrations for testing session'''
    config = Config(ALEMBIC_CONFIG)
    config.set_main_option('sqlalchemy.url', TEST_DATABASE_URI)
    downgrade(config, 'base')


@pytest.fixture(scope='session')
def test_engine():
    '''Creates a DB engine for a testing session'''
    if TEST_DB_PATH.exists():
        TEST_DB_PATH.unlink()

    test_engine = create_engine(TEST_DATABASE_URI)
    apply_migrations()

    yield test_engine

    downgrade_migrations()
    TEST_DB_PATH.unlink()


@pytest.fixture(scope='function')
def test_session(test_engine):
    '''Creates a new database session for a test'''
    connection = test_engine.connect()
    transaction = connection.begin()
    test_db_session = Session(bind=connection)

    yield test_db_session

    test_db_session.close()
    transaction.rollback()
    connection.close()


@pytest.fixture
def artist_repository(test_session):
    return ArtistRepository(db_session=test_session)


@pytest.fixture
def genre_repository(test_session):
    return GenreRepository(db_session=test_session)


@pytest.fixture
def album_repository(test_session):
    return AlbumRepository(db_session=test_session)


# @pytest.fixture
# def music_rating_repository(test_session):
#     return MusicRatingRepository(db_session=test_session)


# @pytest.fixture
# def track_repository(test_session):
#     return TrackRepository(db_session=test_session)

