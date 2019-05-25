from src.dbal import encode_id, decode_id
from src.dbal.models.music_rating import DBALMusicRating
from src.dbal.repositories.dbal_repository import DBALRepository
from src.domain.entities.music_rating import MusicRating


class MusicRatingRepository(DBALRepository):

    def __init__(self, db_session):
        super().__init__(model=DBALMusicRating, db_session=db_session)

    def map_dbal_to_domain(self, dbal_model):
        return MusicRating(
            entity_id=encode_id.music_rating(dbal_model.id),
            artist_id=encode_id.artist(dbal_model.artist_id),
            album_id=encode_id.genre(dbal_model.album_id),
            track_id=encode_id.genre(dbal_model.track_id),
            created_at=dbal_model.created_at,
            updated_at=dbal_model.updated_at,
            rating=dbal_model.rating,
        )

    def map_domain_to_dbal(self, domain_entity):
        return DBALMusicRating(
            id=decode_id.dbal(domain_entity.entity_id),
            artist_id=decode_id.dbal(domain_entity.artist_id),
            album_id=decode_id.dbal(domain_entity.album_id),
            track_id=decode_id.dbal(domain_entity.track_id),
            created_at=domain_entity.created_at,
            updated_at=domain_entity.updated_at,
            rating=domain_entity.rating,
        )
