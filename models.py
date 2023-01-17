from db.database import metadata
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, unique=True, index=True),
    Column("password", String),
    Column("is_active", Boolean, default=True)
)

articles = Table(
    "articles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, index=True),
    Column("article", String),
    Column("owner_id", Integer, ForeignKey("users.id"))
)
