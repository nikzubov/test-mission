from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(
        DateTime,
        default=func.now(),
        onupdate=func.now()
    )


class Users(Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(150), unique=True)


class UserComments(Base):
    __tablename__ = 'usercomments'

    username: Mapped[int] = mapped_column(ForeignKey(Users.username))
    comment: Mapped[str] = mapped_column(Text)
