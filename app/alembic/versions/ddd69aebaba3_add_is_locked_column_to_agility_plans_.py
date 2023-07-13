"""add is_locked column to agility_plans table

Revision ID: ddd69aebaba3
Revises: 3588d123321a
Create Date: 2023-07-12 16:35:45.693829-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column


# revision identifiers, used by Alembic.
revision = "ddd69aebaba3"
down_revision = "3588d123321a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("agility_plans", Column("is_locked", sa.Boolean()))


def downgrade():
    pass
