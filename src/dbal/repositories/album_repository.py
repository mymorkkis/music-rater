from src.dbal import encode_id, decode_id
from src.dbal.models.album import DBALAlbum
from src.dbal.repositories.dbal_repository import DBALRepository
from src.domain.entities.album import Album


class AlbumRepository(DBALRepository):

    def __init__(self, db_session):
        super().__init__(model=DBALAlbum, db_session=db_session)

    def map_dbal_to_domain(self, dbal_model):
        return Album(
            entity_id=encode_id.album(dbal_model.id),
            name=dbal_model.name,
            artist_id=encode_id.artist(dbal_model.artist_id),
            genre_id=encode_id.genre(dbal_model.genre_id),
        )

    def map_domain_to_dbal(self, domain_entity):
        return DBALAlbum(
            id=decode_id.dbal(domain_entity.entity_id),
            name=domain_entity.name,
            artist_id=decode_id.dbal(domain_entity.artist_id),
            genre_id=decode_id.dbal(domain_entity.genre_id),
        )