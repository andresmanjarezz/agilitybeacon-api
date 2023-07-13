from typing import Any, Dict, AnyStr, List
from app.db.dimensions.schemas import DimensionOut
from pydantic import BaseModel
from datetime import datetime
from app.db.users.schemas import UserName


class AssessmentBase(BaseModel):
    name: str = None
    description: str = None
    agility_plan_id: int
    is_locked: bool
    created_by: int = None
    updated_by: int = None


class AssessmentEdit(AssessmentBase):
    class Config:
        orm_mode = True


class AssessmentOut(AssessmentBase):
    id: int
    created_at: datetime = None
    updated_at: datetime = None
    dimensions: List[DimensionOut] = []
    created_by_user: UserName = None
    updated_by_user: UserName = None

    class Config:
        orm_mode = True
