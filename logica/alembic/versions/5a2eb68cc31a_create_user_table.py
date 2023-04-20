"""create user table

Revision ID: 5a2eb68cc31a
Revises: 
Create Date: 2023-02-28 18:32:42.450795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2eb68cc31a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('nick_name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade() -> None:
    op.drop_table('users')
