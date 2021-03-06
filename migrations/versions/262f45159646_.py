"""empty message

Revision ID: 262f45159646
Revises: 
Create Date: 2020-11-10 15:07:36.178321

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '262f45159646'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('phone_number', sa.String(length=18), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=30), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('proposals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('date_of_proposals', sa.DateTime(), nullable=False),
    sa.Column('num_of_roofs', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=False),
    sa.Column('geocoordinates', sa.String(length=80), nullable=False),
    sa.Column('sketchup_model', sa.String(length=60), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roofs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('proposal_id', sa.Integer(), nullable=True),
    sa.Column('pv_panel', sa.Integer(), nullable=True),
    sa.Column('pv_panel_qty', sa.Integer(), nullable=True),
    sa.Column('pv_mount', sa.Integer(), nullable=True),
    sa.Column('pv_cable', sa.Integer(), nullable=True),
    sa.Column('add_construction_qty', sa.Integer(), nullable=True),
    sa.Column('add_construction_price', sa.Integer(), nullable=True),
    sa.Column('azimuth', sa.Integer(), nullable=False),
    sa.Column('angle', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['proposal_id'], ['proposals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solaryeardatas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roof_id', sa.Integer(), nullable=True),
    sa.Column('energy', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roof_id'], ['roofs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solarmonthdatas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year_id', sa.Integer(), nullable=True),
    sa.Column('month', sa.String(length=15), nullable=True),
    sa.Column('energy_perday', sa.Integer(), nullable=True),
    sa.Column('energy', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['year_id'], ['solaryeardatas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('solarhourdatas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('month_id', sa.Integer(), nullable=True),
    sa.Column('hour', sa.Integer(), nullable=True),
    sa.Column('energy', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['month_id'], ['solarmonthdatas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('solarhourdatas')
    op.drop_table('solarmonthdatas')
    op.drop_table('solaryeardatas')
    op.drop_table('roofs')
    op.drop_table('proposals')
    op.drop_table('users')
    op.drop_table('customers')
    # ### end Alembic commands ###
