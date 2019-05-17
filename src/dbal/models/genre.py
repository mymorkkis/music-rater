from sqlalchemy import Column, Integer, String, UniqueConstraint

from src.base import Base


class Genre(Base):
    __tablename__ = 'genre'

    __table_args__ = (
        UniqueConstraint('name'),
    )

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
