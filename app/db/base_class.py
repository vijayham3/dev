# app/db/base_class.py

from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import Column, DateTime, func, Integer

class BaseClass(DeclarativeBase):
    """
    Custom base class for all models.
    Adds common columns like id, created_at, updated_at
    """
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()  # table name is lowercase of class name

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
