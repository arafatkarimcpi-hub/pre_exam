from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql+psycopg2://training_2067_user:3tEErM2v5lMCT0CnDripdKJ9jx1Y8CzY@dpg-dc3qnsjl550s73fa7ubg-a.oregon-postgres.render.com/training_2067"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
