from flask import Flask
from flask_graphql import GraphQLView

from src.base import db_session
from src.graphql.schema import schema, Rating

from src.dbal.artist import Artist
from src.dbal.album import Album
from src.dbal.music_rating import MusicRating

app = Flask(__name__)
app.debug = True

def create_dummy_data():
    artist = Artist(name='Blur', artist_type='solo')
    db_session.add(artist)
    db_session.commit()

    album = Album(title='Parklife', artist_id=artist.id)
    db_session.add(album)
    db_session.commit()

    music_rating = MusicRating(rating=10, artist_id=artist.id, album_id=album.id)
    db_session.add(music_rating)
    db_session.commit()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    create_dummy_data()
    app.run()
