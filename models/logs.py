import sqlalchemy
from sqlalchemy.sql import func
from sqlalchemy import ForeignKeyConstraint

metadata = sqlalchemy.MetaData()

#use sqlalchemy to model table dns
logs = sqlalchemy.Table(
    "logs",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("id_domain", sqlalchemy.Integer),
    sqlalchemy.Column("log", sqlalchemy.Text),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=func.now()),
    sqlalchemy.Column("deleted_at", sqlalchemy.DateTime),

    ForeignKeyConstraint(
        ["id_domain"],
        ["domains.id"],
        use_alter=True,
        onupdate="CASCADE",
        name="fk_element_parent_node_id",
        ondelete="SET NULL",
    ),

)