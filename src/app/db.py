import os

from databases import Database
from sqlalchemy import create_engine, MetaData, Column, Integer, Table, String, DateTime

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("full name", String(50)),
    Column("job title", String(50)),
    Column("employment date", DateTime),
    Column("salary", Integer),
    Column("id chief", Integer),
)

# databases query builder
database = Database(DATABASE_URL)