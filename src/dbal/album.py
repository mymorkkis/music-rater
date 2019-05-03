from sqlalchemy import Column, BigInteger, ForeignKey, String
from sqlalchemy.orm import relationship

from src.base import Base


class Album(Base):
    __tablename__ = 'album'

    id = Column('id', BigInteger, primary_key=True)
    title = Column('title', String(255))
    artist_id = Column(BigInteger, ForeignKey('Artist.id'), nullable=False)
    tracks = relationship('Track', backref='album', lazy=True)
