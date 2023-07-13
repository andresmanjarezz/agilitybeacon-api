from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas
from app.db.core import delete_item


def get_assessment_by_id(db: Session, assessment_id: int):
    try:
        assessment = (
            db.query(models.Assessment)
            .filter(models.Assessment.id == assessment_id)
            .one()
        )

        return assessment
    except:
        return "No result found for query"
