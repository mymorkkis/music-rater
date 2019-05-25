from dataclasses import dataclass

from src.dbal.persistence_generated import PersistenceGeneratedId
from src.domain.entities.domain_entity import DomainEntity


@dataclass
class Artist(DomainEntity):
    name: str
    type_: str
    genre_id: str
    entity_id: str = PersistenceGeneratedId
