"""modify assessments table

Revision ID: 1bf4248835cd
Revises: 0682255807e1
Create Date: 2023-07-05 16:57:03.869373-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Boolean


# revision identifiers, used by Alembic.
revision = "1bf4248835cd"
down_revision = "0682255807e1"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "assessments",
        Column(
            "agility_plan_id", sa.Integer(), sa.ForeignKey("agility_plans.id")
        ),
    )
    op.add_column("assessments", Column("is_locked", sa.Boolean()))


def downgrade():
    pass
