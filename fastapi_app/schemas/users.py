from pydantic import BaseModel


class UsersBase(BaseModel):
    username: str


class UsersCreate(UsersBase):
    pass


class UsersRead(UsersBase):
    id: int
