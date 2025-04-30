import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    password: str


class UserModelRegister(UserBase):
    email: EmailStr


class UserModelLogin(UserBase): ...


class SessionUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: str
    last_login: datetime.datetime
