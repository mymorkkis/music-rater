"""create album table

Revision ID: b0795434405c
Revises: 5118d9c04682
Create Date: 2019-04-28 09:52:32.324245

"""
import sqlalchemy as sa
from alembic import op


revision = 'b0795434405c'
down_revision = '5118d9c04682'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'album',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('artist_id', sa.Integer, sa.ForeignKey('artist.id'), nullable=False)
    )

def downgrade():
    op.drop_table('album')
