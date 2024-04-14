from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import create_engine

import src.config as conf

class Base(DeclarativeBase):
    pass

def get_engine():
    engine = create_engine(
        url=conf.POSTGRES_URL,
        echo=conf.DEV_MODE,
        pool_size=5
    )

    return engine

def create_tables():
    base = Base()
    base.metadata.drop_all(get_engine())
    base.metadata.create_all(get_engine())

def create_session():
    session = sessionmaker(get_engine())

    return session()
