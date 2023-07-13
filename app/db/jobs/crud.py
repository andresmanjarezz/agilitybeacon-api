from fastapi import HTTPException, status
from sqlalchemy.orm import Session
import typing as t
from fastapi.encoders import jsonable_encoder
from . import models, schemas


def get_job(db: Session, job_id: int):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="job not found")
    return job


def get_jobs(
    db: Session, skip: int = 0, limit: int = 100
) -> t.List[schemas.JobOut]:
    return db.query(models.Job).offset(skip).limit(limit).all()


def create_job(db: Session, job: schemas.JobCreate):

    # job_data = jsonable_encoder(job)
    # db_job = models.Job(**job_data)

    db_job = models.Job(
        name=job.name,
        description=job.description,
        application_url_id=job.application_url_id,
    )

    db.add(db_job)
    db.commit()

    db_job_roles = [
        models.JobRole(job_id=db_job.id, role_id=role.id) for role in job.roles
    ]
    db.add_all(db_job_roles)
    db.commit()

    db.refresh(db_job)
    return db_job


def delete_job(db: Session, job_id: int):
    job = get_job(db, job_id)
    if not job:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Job not found")
    db.delete(job)
    db.commit()
    return job


def edit_job(db: Session, job_id: int, job: schemas.JobEdit) -> schemas.Job:
    db_job = get_job(db, job_id)
    if not db_job:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Job not found")
    update_data = job.dict(exclude_unset=True)

    for key, value in update_data.items():
        if key == "roles":
            db_job_roles = [
                models.JobRole(job_id=db_job.id, role_id=role.id)
                for role in job.roles
            ]
            db.add_all(db_job_roles)
            db.commit()
        else:
            setattr(db_job, key, value)

    db.add(db_job)
    db.commit()

    db.refresh(db_job)
    return db_job
