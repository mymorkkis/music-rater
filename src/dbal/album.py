from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from src.base import Base


class Album(Base):
    __tablename__ = 'album'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255))
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable=False)
    tracks = relationship('Track', backref='album', lazy=True)
