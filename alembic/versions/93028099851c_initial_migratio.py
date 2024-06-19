"""Initial migratio

Revision ID: 93028099851c
Revises: 3aa475297827
Create Date: 2024-06-18 19:24:51.916056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93028099851c'
down_revision: Union[str, None] = '3aa475297827'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
