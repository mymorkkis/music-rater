from sqlalchemy import BigInteger, Column, Enum, String
from sqlalchemy.orm import relationship

from src.base import Base


class Artist(Base):
    __tablename__ = 'artist'

    id = Column('id', BigInteger, primary_key=True)
    name = Column('name', String(255), nullable=False)
    artist_type = Column('artist_type', Enum('solo', 'group'), nullable=False)
    albums = relationship('Album', backref='artist', lazy=True)
    tracks = relationship('Track', backref='artist', lazy=True)
