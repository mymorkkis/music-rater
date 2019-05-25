from sqlalchemy import Integer, Column, String, CheckConstraint, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from src.base import Base


class DBALArtist(Base):
    __tablename__ = 'artist'

    __table_args__ = (
        UniqueConstraint('name', 'genre_id', 'artist_type'),
        CheckConstraint('artist_type IN ("solo", "group")', name='artist_type_check'),
    )

    id = Column(Integer, primary_key=True)

    name = Column(String(255), nullable=False, index=True)

    artist_type = Column(String(5), nullable=False)

    genre_id = Column(Integer, ForeignKey('genre.id'), nullable=False)

    albums = relationship('DBALAlbum', backref='artist', lazy=True)

    tracks = relationship('DBALTrack', backref='artist', lazy=True)

    rating = relationship("DBALMusicRating", uselist=False, back_populates="artist")
