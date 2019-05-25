"""Decode GraphQL Base64 id's into int id's used in the DB tables"""
import base64


def dbal(entity_id):
    if not entity_id:
        return

    decoded_id = base64.b64decode(entity_id).decode('utf-8')
    _, db_id = decoded_id.split(':')

    return int(db_id)
