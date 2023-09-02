from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import Integer, String
from db.database import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "username",
        String(255),
    ),
    Column("display_name", String(255)),
    Column("year_of_birth", Integer()),
)

meta.create_all(engine)