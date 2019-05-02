from sqlalchemy import Column, BigInteger, ForeignKey, Integer

from db.engine import Base


class MusicRating(Base):
    __tablename__ = 'music_rating'

    id = Column('id', BigInteger, primary_key=True)
    rating = Column('rating', Integer, nullable=False)
    artist_id = Column(BigInteger, ForeignKey('Artist.id'), nullable=False)
    album_id = Column(BigInteger, ForeignKey('Album.id'), nullable=True)
    track_id = Column(BigInteger, ForeignKey('Track.id'), nullable=True)
