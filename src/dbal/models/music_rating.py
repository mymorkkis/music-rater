from sqlalchemy import Column, DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import relationship

from src.base import Base


class DBALMusicRating(Base):
    __tablename__ = 'music_rating'

    id = Column(Integer, primary_key=True)

    rating = Column(Integer, nullable=False)

    created_at = Column(DateTime, nullable=False, server_default=func.current_timestamp())

    updated_at = Column(DateTime, nullable=True, onupdate=func.current_timestamp())

    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)

    album_id = Column(Integer, ForeignKey('album.id'), nullable=True)

    track_id = Column(Integer, ForeignKey('track.id'), nullable=True)

    artist = relationship("DBALArtist", back_populates="rating")

    album = relationship("DBALAlbum", back_populates="rating")

    track = relationship("DBALTrack", back_populates="rating")
