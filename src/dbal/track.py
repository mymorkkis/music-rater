from sqlalchemy import Column, BigInteger, ForeignKey, String

from db.engine import Base


class Track(Base):
    __tablename__ = 'track'

    id = Column('id', BigInteger, primary_key=True)
    title = Column('title', String(255), nullable=False)
    artist_id = Column(BigInteger, ForeignKey('Artist.id'), nullable=False)
    album_id = Column(BigInteger, ForeignKey('Album.id'), nullable=True)
