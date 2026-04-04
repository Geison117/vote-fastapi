"""add content column to post table

Revision ID: 772954aba6f2
Revises: 103810aac227
Create Date: 2026-04-02 11:53:24.060570

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '772954aba6f2'
down_revision: Union[str, Sequence[str], None] = '103810aac227'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
