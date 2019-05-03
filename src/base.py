from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

sqlite_db = {'drivername': 'sqlite', 'database': 'music_rater_graphql.db'}

Base = declarative_base()

engine = create_engine(URL(**sqlite_db))

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base.metadata.create_all(engine)

Base.query.db_session.query_property()
