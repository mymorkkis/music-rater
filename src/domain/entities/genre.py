from dataclasses import dataclass

from src.dbal.persistence_generated import PersistenceGeneratedId
from src.domain.entities.domain_entity import DomainEntity


@dataclass
class Genre(DomainEntity):
    name: str
    entity_id: str = PersistenceGeneratedId
