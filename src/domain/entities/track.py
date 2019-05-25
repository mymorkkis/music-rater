from dataclasses import dataclass
from typing import Optional

from src.dbal.persistence_generated import PersistenceGeneratedId
from src.domain.entities.domain_entity import DomainEntity


@dataclass
class Track(DomainEntity):
    name: str
    artist_id: str
    genre_id: str
    album_id: Optional[str] = None
    entity_id: str = PersistenceGeneratedId
