"""Renaming students to scholars

Revision ID: 1a7c0dc962c5
Revises: 791279dd0760
Create Date: 2023-03-06 16:49:39.791067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a7c0dc962c5'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    op.alter_column('scholars', 'name', new_column_name='names')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
