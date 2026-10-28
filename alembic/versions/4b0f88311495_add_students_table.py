"""add students table

Revision ID: 4b0f88311495
Revises: 1832079b6801
Create Date: 2026-10-28 20:29:12.421575

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b0f88311495'
down_revision: Union[str, Sequence[str], None] = '1832079b6801'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
