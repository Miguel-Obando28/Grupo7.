"""add students table

Revision ID: 1832079b6801
Revises: a74cd0d4fac0
Create Date: 2026-10-28 19:58:26.518992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1832079b6801'
down_revision: Union[str, Sequence[str], None] = 'a74cd0d4fac0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
