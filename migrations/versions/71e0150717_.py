"""empty message

Revision ID: 71e0150717
Revises: None
Create Date: 2016-04-24 11:44:07.026013

"""

# revision identifiers, used by Alembic.
revision = '71e0150717'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('spend')
    op.drop_table('promotions')
    op.drop_table('customers')
    op.drop_table('periods')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('periods',
    sa.Column('period', sa.DATE(), nullable=False),
    sa.Column('year', sa.INTEGER(), nullable=False),
    sa.Column('quarter', sa.VARCHAR(length=7), nullable=False),
    sa.PrimaryKeyConstraint('period')
    )
    op.create_table('customers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=900), nullable=False),
    sa.Column('record_type', sa.VARCHAR(length=20), nullable=False),
    sa.Column('country_code', sa.VARCHAR(length=2), nullable=True),
    sa.Column('state', sa.VARCHAR(length=100), nullable=True),
    sa.Column('city', sa.VARCHAR(length=100), nullable=True),
    sa.Column('tier', sa.VARCHAR(length=6), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('promotions',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=1000), nullable=False),
    sa.Column('credit_name', sa.VARCHAR(length=600), nullable=False),
    sa.Column('credit_value', sa.NUMERIC(precision=30, scale=6), nullable=False),
    sa.Column('credit_remaining_value', sa.NUMERIC(precision=30, scale=6), nullable=False),
    sa.Column('redeemed_date', sa.DATE(), nullable=True),
    sa.Column('expiration_date', sa.DATE(), nullable=False),
    sa.Column('customer_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('spend',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('period', sa.DATE(), nullable=True),
    sa.Column('promotion_id', sa.INTEGER(), nullable=True),
    sa.Column('product_id', sa.INTEGER(), nullable=True),
    sa.Column('customer_id', sa.INTEGER(), nullable=True),
    sa.Column('spend', sa.NUMERIC(precision=30, scale=6), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['period'], ['periods.period'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['promotion_id'], ['promotions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=900), nullable=True),
    sa.Column('category', sa.VARCHAR(length=900), nullable=False),
    sa.Column('sub_category', sa.VARCHAR(length=900), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###
