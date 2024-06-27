from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.orm import (orm_get_users, orm_add_users,
                          orm_add_comments, orm_get_comments)
from database.engine import database
from schemas.users import CommentsCreate, CommentsRead, UsersRead, UsersCreate

router = APIRouter()


@router.post('/users-add/')
async def add_users(
    users_create: UsersCreate,
    session: AsyncSession = Depends(database.get_session),
):
    users = await orm_add_users(session=session, users_create=users_create)
    return users


@router.get('/users/', response_model=List[UsersRead])
async def get_users(
    session: AsyncSession = Depends(database.get_session)
):
    users = await orm_get_users(session=session)
    return users


@router.get('/comments/', response_model=List[CommentsRead])
async def get_comments(
    session: AsyncSession = Depends(database.get_session)
):
    comments = await orm_get_comments(session=session)
    return comments


@router.post('/comments-add/')
async def add_comments(
    comments_create: CommentsCreate,
    session: AsyncSession = Depends(database.get_session)
):
    comments = await orm_add_comments(
        session=session,
        comments_create=comments_create
    )
    return comments
