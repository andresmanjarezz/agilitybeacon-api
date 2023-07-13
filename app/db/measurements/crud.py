from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t

from . import models, schemas
from app.db.measurements.models import Measurement
from app.db.users.models import User
from app.db.core import delete_item


def get_measurements_by_objective_id(db: Session, objective_id):
    items = (
        db.query(Measurement)
        .filter(Measurement.objective_id == objective_id)
        .order_by(Measurement.created_at)
        .all()
    )
    for measurement in items:
        user = db.query(User).filter(User.id == measurement.created_by).one()
        measurement.created_by = user.first_name
    return items
