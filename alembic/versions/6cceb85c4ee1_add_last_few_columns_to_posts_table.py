"""add last few columns to posts table

Revision ID: 6cceb85c4ee1
Revises: af4457408543
Create Date: 2026-04-02 12:32:35.090568

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6cceb85c4ee1'
down_revision: Union[str, Sequence[str], None] = 'af4457408543'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', 
                  sa.Column('published', 
                            sa.Boolean(), 
                            nullable=False, 
                            server_default='TRUE'))
    op.add_column('posts', 
                  sa.Column('created_at', 
                            sa.TIMESTAMP(timezone=True), 
                            server_default=sa.text('now()'), 
                            nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
