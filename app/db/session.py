from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# -------------------------
# Database URL (SQLite for dev, can switch to Postgres/MySQL)
# -------------------------
SQLALCHEMY_DATABASE_URL = "postgresql://sitara_user:sitara@localhost:5432/sitara"  # relative path

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# -------------------------
# Dependency to get DB session
# -------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
