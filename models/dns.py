import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy import ForeignKeyConstraint

metadata = sqlalchemy.MetaData()

#use sqlalchemy to model table dns
dnsTable = sqlalchemy.Table(
    "dns",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("dns", sqlalchemy.String),
    sqlalchemy.Column("id_domain", sqlalchemy.Integer),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=func.now()),
    sqlalchemy.Column("state", sqlalchemy.SmallInteger),

    ForeignKeyConstraint(
        ["id_domain"],
        ["domains.id"],
        use_alter=True,
        onupdate="CASCADE",
        name="fk_element_parent_node_id",
        ondelete="SET NULL",
    ),

)