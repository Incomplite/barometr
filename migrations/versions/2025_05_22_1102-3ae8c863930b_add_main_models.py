"""Add main models

Revision ID: 3ae8c863930b
Revises: e9d24d760fe9
Create Date: 2025-05-22 11:02:39.757920

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ae8c863930b'
down_revision: Union[str, None] = 'e9d24d760fe9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('address', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bar_and_tag_association',
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.PrimaryKeyConstraint('bar_id', 'tag_id')
    )
    op.create_table('bars_gallery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cocktails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('ingredients', sa.Text(), nullable=False),
    sa.Column('recipe', sa.Text(), nullable=False),
    sa.Column('video_url', sa.String(length=200), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review_bar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_favorite_bar_association',
    sa.Column('bar_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bar_id'], ['bars.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('bar_id', 'user_id')
    )
    op.create_table('cocktails_gallery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=200), nullable=False),
    sa.Column('cocktail_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cocktail_id'], ['cocktails.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review_cocktail',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('cocktail_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cocktail_id'], ['cocktails.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review_cocktail')
    op.drop_table('cocktails_gallery')
    op.drop_table('user_favorite_bar_association')
    op.drop_table('review_bar')
    op.drop_table('cocktails')
    op.drop_table('bars_gallery')
    op.drop_table('bar_and_tag_association')
    op.drop_table('tags')
    op.drop_table('bars')
    # ### end Alembic commands ###
