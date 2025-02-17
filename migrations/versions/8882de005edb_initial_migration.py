"""Initial migration

Revision ID: 8882de005edb
Revises: 
Create Date: 2024-08-05 09:24:03.774319

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8882de005edb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalogues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('brand', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('price', sa.String(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=False),
    sa.Column('release_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_catalogues'))
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_users')),
    sa.UniqueConstraint('email', name=op.f('uq_users_email')),
    sa.UniqueConstraint('username', name=op.f('uq_users_username'))
    )
    op.create_table('addcatalogues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=False),
    sa.Column('brand', sa.Text(), nullable=False),
    sa.Column('model', sa.Text(), nullable=False),
    sa.Column('category', sa.Text(), nullable=False),
    sa.Column('price', sa.Text(), nullable=False),
    sa.Column('rating', sa.Text(), nullable=False),
    sa.Column('release_date', sa.Text(), nullable=False),
    sa.Column('catalogue_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['catalogue_id'], ['catalogues.id'], name=op.f('fk_addcatalogues_catalogue_id_catalogues')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_addcatalogues_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_addcatalogues'))
    )
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.Column('ticket_price', sa.String(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('catalogue_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['catalogue_id'], ['catalogues.id'], name=op.f('fk_news_catalogue_id_catalogues')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_news_user_id_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_news'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    op.drop_table('addcatalogues')
    op.drop_table('users')
    op.drop_table('catalogues')
    # ### end Alembic commands ###
