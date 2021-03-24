"""Init tables

Revision ID: 275515c51af1
Revises:
Create Date: 2021-03-24 15:03:16.549798

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "275515c51af1"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "comments_threads",
        sa.Column("id", sa.Text, primary_key=True),
        sa.Column("object_id", sa.Text, nullable=False),
        sa.Column("object_type", sa.Text, nullable=False),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.current_timestamp(),
        ),
    )
    op.create_table(
        "comments_comments",
        sa.Column("id", sa.Text, primary_key=True),
        sa.Column(
            "thread_id",
            sa.Text,
            sa.ForeignKey("comments_threads.id"),
            nullable=False,
        ),
        sa.Column("author_id", sa.Text, nullable=False),
        sa.Column("author_type", sa.Text, nullable=False),
        sa.Index("author_idx", "author_id", "author_type"),
        sa.Column(
            "reply_to_id",
            sa.Text,
            sa.ForeignKey("comments_comments.id"),
            nullable=True,
            index=True,
        ),
        sa.Column(
            "created_at",
            sa.DateTime,
            nullable=False,
            server_default=sa.func.current_timestamp(),
        ),
        sa.Column("modified_at", sa.DateTime, nullable=True),
    )


def downgrade():
    op.drop_table("comments_comments")
    op.drop_table("comments_threads")
