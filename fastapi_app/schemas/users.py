from pydantic import BaseModel


class UsersBase(BaseModel):
    username: str


class UsersCreate(UsersBase):
    pass


class UsersRead(UsersBase):
    id: int


class UserComments(BaseModel):
    username: str
    comment: str


class CommentsCreate(UserComments):
    pass


class CommentsRead(UserComments):
    id: int
