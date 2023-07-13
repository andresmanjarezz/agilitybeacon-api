from ctypes import Union
from pydantic import BaseModel, Field
import typing as t
from app.db.roles.schemas import Role
from app.db.jobs.schemas import Job
from typing import List


class UseCaseBase(BaseModel):
    name: str = None
    description: str = None
    table_config: str = None


class UseCaseCreate(UseCaseBase):
    name: str
    role_ids: List[int] = []
    job_ids: List[int] = []

    class Config:
        orm_mode = True


class UseCaseEdit(UseCaseBase):
    role_ids: List[int] = []
    job_ids: List[int] = []

    class Config:
        orm_mode = True


class UseCaseMapping(BaseModel):
    id: int
    use_case_id: int = None
    job_id: int = None
    role_id: int = None


class UseCase(UseCaseBase):
    id: int
    roles: List[Role] = None
    role_ids: List[int] = []
    jobs: List[Job] = None
    job_ids: List[int] = []
    use_case_mapping: List[UseCaseMapping] = []

    class Config:
        orm_mode = True
