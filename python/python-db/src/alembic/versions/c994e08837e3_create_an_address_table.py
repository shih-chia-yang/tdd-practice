"""create an address table

Revision ID: c994e08837e3
Revises: 
Create Date: 2021-03-16 14:06:35.843469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c994e08837e3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id',sa.Integer,primary_key=True),
        sa.Column('address',sa.String(50),nullable=False),
        sa.Column('city',sa.String(50),nullable=False),
        sa.Column('state',sa.String(20),nullable=False),
    )


def downgrade():
    op.drop_table('address')
