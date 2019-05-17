import pytest

from src.domain.music_rating_entity import MusicRating
from src.domain.music_rating_repository import MusicRatingRepository


@pytest.fixture
def music_rating():
    return MusicRating(
        entity_id='TXVzaWNSYXRpbmc6MQ==',
        artist_name='Blur',
        artist_type='Group',
        genre_name='Indie',
        rating=7,
        track_name='Song 2',
    )

class TestMusicRatingRepository:

    def test_repository_can_be_instantiated(self, music_rating, mock_dbal_repository):
        repository = MusicRatingRepository(entity=music_rating, repository=mock_dbal_repository)
        assert repository.entity == music_rating
        assert repository.repository == mock_dbal_repository
