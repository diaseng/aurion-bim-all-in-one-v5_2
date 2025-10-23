
from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'sinapi_items',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('code', sa.String(length=64), nullable=False, unique=True),
        sa.Column('description', sa.String(length=512), nullable=False),
        sa.Column('unit', sa.String(length=16), nullable=False),
        sa.Column('price', sa.Float(), nullable=False),
    )
    op.create_index('ix_sinapi_code', 'sinapi_items', ['code'], unique=True)

def downgrade():
    op.drop_index('ix_sinapi_code', table_name='sinapi_items')
    op.drop_table('sinapi_items')
