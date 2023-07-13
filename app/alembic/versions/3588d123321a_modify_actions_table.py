"""modify actions table

Revision ID: 3588d123321a
Revises: 66e27d02b2d7
Create Date: 2023-07-12 15:55:29.549060-07:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column
from app.db.enums import ActionStatus, ActionType
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "3588d123321a"
down_revision = "66e27d02b2d7"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("actions", "name")
    op.drop_column("actions", "description")
    op.drop_column("actions", "is_active")
    op.drop_column("actions", "playbook_id")
    op.add_column("actions", Column("object_id", sa.Integer()))
    op.add_column("actions", Column("org_type_id", sa.Integer()))
    op.add_column("actions", Column("timezone", sa.String()))
    op.add_column(
        "actions",
        Column(
            "start_datetime",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
        ),
    )
    op.add_column(
        "actions",
        Column(
            "end_datetime",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"),
        ),
    )
    op.execute("ALTER TABLE actions DROP COLUMN action_type;")
    op.execute("DROP TYPE action_type_enum;")
    action_type_enum = postgresql.ENUM(ActionType, name="action_type_enum")
    action_type_enum.create(op.get_bind())
    op.add_column(
        "actions",
        sa.Column("action_type", action_type_enum, nullable=True),
    )
    action_status_enum = postgresql.ENUM(
        ActionStatus, name="action_status_enum"
    )
    action_status_enum.create(op.get_bind())
    op.add_column(
        "actions",
        sa.Column("status", action_status_enum, nullable=True),
    )
    op.add_column("actions", Column("order", sa.Integer()))


def downgrade():
    pass
