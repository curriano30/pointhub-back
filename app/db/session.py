from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Asegúrate de reemplazar 'user', 'password', 'localhost' y 'dbname' con tus datos reales
SQLALCHEMY_DATABASE_URL = "postgresql://main:main.tester@localhost/pointhub"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
