from sqlalchemy import Integer, Column, String, CheckConstraint
from sqlalchemy.orm import relationship

from src.base import Base


class Artist(Base):
    __tablename__ = 'artist'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(255), nullable=False)
    artist_type = Column('artist_type', String(5), CheckConstraint('artist_type IN ("solo", "group")'), nullable=False)
    albums = relationship('Album', backref='artist', lazy=True)
    tracks = relationship('Track', backref='artist', lazy=True)
