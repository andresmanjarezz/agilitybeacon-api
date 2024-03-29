from typing import List
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from app.db.session import Base
from app.db.core import CoreBase, TrackTimeMixin
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON


class Question(Base, CoreBase, TrackTimeMixin):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    dimension_id = Column(Integer, ForeignKey("dimensions.id"), nullable=True)
    baseline_value = Column(Numeric)
    target_value = Column(Numeric)
