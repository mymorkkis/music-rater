from sqlalchemy import Column, Integer, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import relationship

from src.base import Base


class DBALAlbum(Base):
    __tablename__ = 'album'

    __table_args__ = (
        UniqueConstraint('name', 'artist_id'),
    )

    id = Column(Integer, primary_key=True)

    name = Column(String(255), index=True)

    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)

    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)

    tracks = relationship('DBALTrack', backref='album', lazy=True)

    rating = relationship("DBALMusicRating", uselist=False, back_populates="album")
