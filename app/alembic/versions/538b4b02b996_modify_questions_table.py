"""modify questions table

Revision ID: 538b4b02b996
Revises: 1bf4248835cd
Create Date: 2023-07-05 18:07:06.366064-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column


# revision identifiers, used by Alembic.
revision = "538b4b02b996"
down_revision = "1bf4248835cd"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("questions", Column("baseline_value", sa.Numeric()))
    op.add_column("questions", Column("target_value", sa.Numeric()))


def downgrade():
    pass
