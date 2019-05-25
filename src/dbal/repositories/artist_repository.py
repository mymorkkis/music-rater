from src.dbal import encode_id, decode_id
from src.dbal.models.artist import DBALArtist
from src.dbal.repositories.dbal_repository import DBALRepository
from src.domain.entities.artist import Artist


class ArtistRepository(DBALRepository):

    def __init__(self, db_session):
        super().__init__(model=DBALArtist, db_session=db_session)

    def map_dbal_to_domain(self, dbal_model):
        return Artist(
            entity_id=encode_id.artist(dbal_model.id),
            name=dbal_model.name,
            type_=dbal_model.artist_type,
            genre_id=encode_id.genre(dbal_model.genre_id),
        )

    def map_domain_to_dbal(self, domain_entity):
        return DBALArtist(
            id=decode_id.dbal(domain_entity.entity_id),
            name=domain_entity.name,
            artist_type=domain_entity.type_,
            genre_id=decode_id.dbal(domain_entity.genre_id),
        )