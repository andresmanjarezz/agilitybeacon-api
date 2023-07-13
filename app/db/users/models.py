from sqlalchemy import Boolean, Column, Integer, String

from app.db.session import Base
from app.db.core import CoreBase, TrackTimeMixin


class User(Base, CoreBase, TrackTimeMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    role_id = Column(Integer)
    is_designer = Column(Boolean, default=False)
