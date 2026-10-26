"""initial migration

Revision ID: a74cd0d4fac0
Revises: 0e2a7458d010
Create Date: 2026-10-26 09:04:40.917805

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a74cd0d4fac0'
down_revision: Union[str, Sequence[str], None] = '0e2a7458d010'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
