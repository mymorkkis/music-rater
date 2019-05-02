from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

sqlite_db = {'drivername': 'sqlite', 'database': 'music_rater_graphql.db'}

Base = declarative_base()

engine = create_engine(URL(**sqlite_db))

Base.metadata.create_all(engine)
