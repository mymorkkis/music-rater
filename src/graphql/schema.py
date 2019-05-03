import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from src.dbal import artist, album, music_rating, track


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
        interfaces = (relay.Node, Artist, Rating)


class Track(SQLAlchemyObjectType):
    class Meta:
        model = track.Track
        interfaces = (relay.Node, Artist, Rating)


class RatingConnection(relay.Connection):
    class Meta:
        node = Rating


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_ratings = SQLAlchemyConnectionField(RatingConnection)

schema = graphene.Schema(query=Query)
