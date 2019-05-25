from abc import ABC, abstractmethod

from sqlalchemy.orm.exc import NoResultFound

from src.dbal import decode_id


class NotFound(Exception):
    pass


class DBALRepository(ABC):

    def __init__(self, model, db_session):
        self.model = model
        self.session = db_session

    def get_by_id(self, entity_id):
        dbal_entity = self._get_dbal_entity(entity_id)
        return self.map_dbal_to_domain(dbal_entity)

    def _get_dbal_entity(self, entity_id):
        dbal_id = decode_id.dbal(entity_id)
        try:
            return self.session.query(self.model).filter_by(id=dbal_id).one()
        except NoResultFound:
            raise NotFound(f'Entity: {self.model.__tablename__} could not be found')

    def find(self, **attributes):
        # Basic implementation handling eq. TODO Flesh out with proper criterion login
        query = self.session.query(self.model)
        for key, value in attributes.items():
            query = query.filter(getattr(self.model, key) == value)
        return [self.map_dbal_to_domain(dbal_entity) for dbal_entity in query.all()]

    def add(self, entity):
        dbal_entity = self.map_domain_to_dbal(entity)
        self.session.add(dbal_entity)
        self.session.commit()
        return self.map_dbal_to_domain(dbal_entity)

    def delete(self, entity):
        dbal_entity = self._get_dbal_entity(entity.entity_id)
        self.session.delete(dbal_entity)
        self.session.commit()

    def update(self, entity):
        dbal_entity = self.map_domain_to_dbal(entity)
        self.session.merge(dbal_entity)
        self.session.commit()
        return self.map_dbal_to_domain(dbal_entity)

    def upsert(self, entity):
        try:
            stored_entity = self.get_by_id(entity.entity_id)
            return self.update(stored_entity)
        except NotFound:
            return self.add(entity)

    def truncate_table(self):
        self.session.query(self.model).delete()
        self.session.commit()

    @abstractmethod
    def map_dbal_to_domain(self, dbal_model):
        return NotImplemented

    @abstractmethod
    def map_domain_to_dbal(self, domain_entity):
        return NotImplemented
