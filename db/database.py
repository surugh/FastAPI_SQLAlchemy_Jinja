import databases
from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = "sqlite:///db/database.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# metadata - объект, по сути, представляет собой фасад вокруг словаря Python,
# в котором хранится ряд Table объектов, привязанных к их строковым именам
# https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
metadata = MetaData()
# создаем объект database, который будет использоваться для выполнения запросов
database = databases.Database(SQLALCHEMY_DATABASE_URL)
# соединяемся
engine = create_engine(SQLALCHEMY_DATABASE_URL)
