from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from dotenv import load_dotenv
from os import getenv


load_dotenv()
DB_NAME = getenv('DB_NAME')
DB_PASS = getenv('DB_PASS')
DB_USER = getenv('DB_USER')
DB_PORT = getenv('DB_PORT')
DB_HOST = getenv('DB_HOST')


engine = create_engine(
    f'postgresql://{DB_NAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    