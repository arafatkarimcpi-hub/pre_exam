from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "postgresql+psycopg2://training_8nwk_user:3UuuPLx0Lx1cB5bAI8U79Q1netU5K7K0@dpg-dc3rdotg1s2s73cgo560-a.oregon-postgres.render.com/training_8nwk"
engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
base = declarative_base()


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
