from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import Integer, String, ForeignKey, Text, DateTime, UUID
from sqlalchemy import func
from datetime import datetime
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
    f'postgresql+psycopg2://{DB_NAME}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    echo = True,
    )


class Base(DeclarativeBase):
    pass


class Question(Base):
    __tablename__ = "question"
    id = mapped_column(Integer, primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    def __repr__(self) -> str:
        return f'Question(id={self.id!r}, text={self.text!r}, created_at={self.created_at!r})'


class Answer(Base):
    __tablename__ = "answer"
    id = mapped_column(Integer, primary_key=True)
    question_id: Mapped[int] = mapped_column(ForeignKey("Question.id"))
    user_id: Mapped[str] = mapped_column(UUID)
    text: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())

    def __repr__(self) -> str:
        return f'Answer(id={self.id!r}, question_id={self.question_id!r},' \
            f'user_id={self.user_id!r}, text={self.text!r},' \
                 f' created_at={self.created_at!r})'
