"""new fields in user model

Revision ID: 467734c2d0cf
Revises: dafa9d4e397c
Create Date: 2023-03-15 15:01:19.210583

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '467734c2d0cf'
down_revision = 'dafa9d4e397c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
