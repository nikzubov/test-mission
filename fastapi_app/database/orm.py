from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence
from schemas.users import UsersCreate, CommentsCreate
from database.models import Users, UserComments


async def orm_get_users(
    session: AsyncSession
) -> Sequence[Users]:
    users = await session.execute(select(Users))
    result = users.scalars()
    return result.all()


async def orm_add_users(
    session: AsyncSession,
    users_create: UsersCreate
) -> Users:
    users = Users(**users_create.model_dump())
    user = await session.execute(
        select(Users)
        .where(Users.username == users.username)
    )
    if not user.first():
        session.add(users)
        await session.commit()
        return users


async def orm_get_comments(
    session: AsyncSession,
) -> Sequence[UserComments]:
    comments = await session.execute(select(UserComments))
    result = comments.scalars()
    return result


async def orm_add_comments(
    session: AsyncSession,
    comments_create: CommentsCreate
) -> UserComments:
    comments = UserComments(**comments_create.model_dump())
    users_check = await session.execute(
        select(Users)
        .where(Users.username == comments.username)
    )
    if not users_check.first():
        return
    session.add(comments)
    await session.commit()
    return comments
