from sqlalchemy import Column, Integer, String

from src.base import Base


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, index=True)
