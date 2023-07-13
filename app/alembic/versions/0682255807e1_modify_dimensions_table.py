"""modify dimensions table

Revision ID: 0682255807e1
Revises: e764496bf2d6
Create Date: 2023-07-05 16:51:38.373220-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Boolean


# revision identifiers, used by Alembic.
revision = "0682255807e1"
down_revision = "e764496bf2d6"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("dimensions", "baseline_value")
    op.drop_column("dimensions", "ideal_value")


def downgrade():
    pass
