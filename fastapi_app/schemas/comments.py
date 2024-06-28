from pydantic import BaseModel


class UserComments(BaseModel):
    username: str
    comment: str


class CommentsCreate(UserComments):
    pass


class CommentsRead(UserComments):
    id: int