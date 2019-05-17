from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DBALRepository():

    def __init__(self, model, db_session):
        self.model = model
        self.session = db_session

    def get(self, entity_id):
        return self.session.query(self.model).filter_by(id=entity_id).one()

    def add(self, entity):
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, entity):
        try:
            self.session.delete(entity)
            self.session.commit()
        except InvalidRequestError:
            pass  # TODO Log error?

    def update(self, entity):
        stored_entity = self.get(entity.id)

        for attribute in vars(stored_entity).keys():
            if not attribute.startswith('_'):
                setattr(stored_entity, attribute, getattr(entity, attribute))

        self.session.commit()
        return stored_entity

    def upsert(self, entity):
        try:
            stored_entity = self.get(entity.id)
            return self.update(stored_entity)
        except NoResultFound:
            return self.add(entity)
