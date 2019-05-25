from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from src.dbal.persistence_generated import PersistenceGeneratedId
from src.domain.entities.domain_entity import DomainEntity


@dataclass
class MusicRating(DomainEntity):
    rating: int
    artist_id: str
    album_id: Optional[str] = None
    track_id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    entity_id: str = PersistenceGeneratedId
