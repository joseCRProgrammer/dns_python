import sqlalchemy
from sqlalchemy.sql import func

metadata = sqlalchemy.MetaData()

#use sqlalchemy to model table dns
domains = sqlalchemy.Table(
    "domains",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("domain", sqlalchemy.String, unique=True),
    sqlalchemy.Column("description", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, server_default=func.now()),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime, onupdate=func.now()),
    sqlalchemy.Column("deleted_at", sqlalchemy.DateTime),
)


