from typing import Optional
from pydantic import BaseModel, validator


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    id: int
    username: str

    @validator("id")
    def name_must_contain_space(cls, v):
        return v + 1

    class Config:
        orm_mode = True
