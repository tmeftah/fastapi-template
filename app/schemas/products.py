from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True
