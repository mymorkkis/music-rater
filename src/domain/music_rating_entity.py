from dataclasses import dataclass
from typing import Optional

from src.domain.domain_entity import DomainEntity


@dataclass
class MusicRating(DomainEntity):
    entity_id: str
    artist_name: str
    artist_type: str
    genre_name: str
    rating: int
    album_name: Optional[str] = None
    track_name: Optional[str] = None
