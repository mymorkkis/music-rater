from dataclasses import dataclass

from src.dbal.dbal_repository import DBALRepository
from src.domain.domain_entity import DomainEntity


@dataclass
class MusicRatingRepository:
    entity: DomainEntity
    repository: DBALRepository
