from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from src.base import Base


class Track(Base):
    __tablename__ = 'track'

    __table_args__ = (
        UniqueConstraint('name', 'artist_id'),
        UniqueConstraint('name', 'album_id'),
    )

    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False, index=True)

    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)

    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)

    album_id = Column(Integer, ForeignKey('album.id'), nullable=True)

    rating = relationship("MusicRating", uselist=False, back_populates="track")
