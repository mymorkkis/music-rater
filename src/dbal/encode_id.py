"""Encode DB int id's into Base64 id's used by GraphQL. Format: 'CamelCaseTableName:INT_ID'"""
import base64


def artist(db_id):
    return _encode_domain_id(prefix='Artist', db_id=db_id)


def album(db_id):
    return _encode_domain_id(prefix='Album', db_id=db_id)


def genre(db_id):
    return _encode_domain_id(prefix='Genre', db_id=db_id)


def music_rating(db_id):
    return _encode_domain_id(prefix='MusicRating', db_id=db_id)


def track(db_id):
    return _encode_domain_id(prefix='Track', db_id=db_id)


def _encode_domain_id(prefix, db_id):
    domain_id = f'{prefix}:{db_id}'
    return base64.b64encode(domain_id.encode())
