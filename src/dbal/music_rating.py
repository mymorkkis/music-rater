from datetime import datetime

from sqlalchemy import Column, BigInteger, DateTime, ForeignKey, Integer

from src.base import Base


class MusicRating(Base):
    __tablename__ = 'music_rating'

    id = Column('id', BigInteger, primary_key=True)
    rating = Column('rating', Integer, nullable=False)
    created_at = Column('created_at', DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column('updated_at', DateTime, nullable=True)
    artist_id = Column(BigInteger, ForeignKey('Artist.id'), nullable=False)
    album_id = Column(BigInteger, ForeignKey('Album.id'), nullable=True)
    track_id = Column(BigInteger, ForeignKey('Track.id'), nullable=True)
