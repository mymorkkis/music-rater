from src.dbal import encode_id, decode_id
from src.dbal.models.genre import DBALGenre
from src.domain.entities.genre import Genre
from src.dbal.repositories.dbal_repository import DBALRepository


class GenreRepository(DBALRepository):

    def __init__(self, db_session):
        super().__init__(model=DBALGenre, db_session=db_session)

    def map_dbal_to_domain(self, dbal_model):
        return Genre(
            entity_id=encode_id.genre(dbal_model.id),
            name=dbal_model.name,
        )

    def map_domain_to_dbal(self, domain_entity):
        return DBALGenre(
            id=decode_id.dbal(domain_entity.entity_id),
            name=domain_entity.name,
        )
