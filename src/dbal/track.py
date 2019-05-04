from sqlalchemy import Column, Integer, ForeignKey, String

from src.base import Base


class Track(Base):
    __tablename__ = 'track'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)
    album_id = Column(Integer, ForeignKey('album.id'), nullable=True)
