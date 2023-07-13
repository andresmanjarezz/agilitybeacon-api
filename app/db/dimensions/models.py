from typing import List
from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from app.db.session import Base
from app.db.core import CoreBase, TrackTimeMixin
from sqlalchemy import orm
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSON
from fastapi import HTTPException


class Dimension(Base, CoreBase, TrackTimeMixin):
    __tablename__ = "dimensions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    assessment_id = Column(Integer, ForeignKey("assessments.id"), nullable=True)
