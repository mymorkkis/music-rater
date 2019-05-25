from abc import ABC


class DomainEntity(ABC):
    def __init__(self):
        self.entity_id = None
