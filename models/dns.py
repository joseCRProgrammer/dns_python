import sqlalchemy

metadata = sqlalchemy.MetaData()

#use sqlalchemy to model table dns
dns = sqlalchemy.Table(
    "dns",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("dns", sqlalchemy.String),
    sqlalchemy.Column("description", sqlalchemy.String),

)


