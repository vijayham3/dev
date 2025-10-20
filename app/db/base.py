# app/db/base.py

from sqlalchemy.orm import declarative_base

# Create the SQLAlchemy Base class
Base = declarative_base()

# Import all models here so Alembic can detect them
# from app.models.user import User
# from app.models.product import Product
# from app.models.order import Order
# from app.models.cart import Cart
