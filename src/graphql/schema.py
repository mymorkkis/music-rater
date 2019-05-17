import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from src.dbal.models import artist, album, track, music_rating, genre


class Rating(SQLAlchemyObjectType):
    class Meta:
        model = music_rating.MusicRating
        interfaces = (relay.Node, )


class Artist(SQLAlchemyObjectType):
    class Meta:
        model = artist.Artist
        interfaces = (relay.Node, )


class Album(SQLAlchemyObjectType):
    class Meta:
        model = album.Album
        interfaces = (relay.Node, )


class Track(SQLAlchemyObjectType):
    class Meta:
        model = track.Track
        interfaces = (relay.Node, )


class Genre(SQLAlchemyObjectType):
    class Meta:
        model = genre.Genre
        interfaces = (relay.Node, )


class RatingConnection(relay.Connection):
    class Meta:
        node = Rating


class AlbumConnections(relay.Connection):
    class Meta:
        node = Album


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_ratings = SQLAlchemyConnectionField(RatingConnection)

    all_albums = SQLAlchemyConnectionField(AlbumConnections, sort=None)


schema = graphene.Schema(query=Query)
