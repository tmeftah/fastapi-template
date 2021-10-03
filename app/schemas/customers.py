from typing import Optional
from pydantic import BaseModel, EmailStr, AnyHttpUrl, validator


class CustomerBase(BaseModel):
    name: str
    address: EmailStr
    postcode: Optional[str] = None
    town: Optional[str] = None
    salutation: Optional[str] = None
    phone: Optional[str] = None
    fax: Optional[str] = None
    website: Optional[AnyHttpUrl] = None
    Remarks: Optional[str] = None

    @validator("name", "town")
    def name_must_have_5_characters(cls, v):
        if v != None and len(v) < 5:
            raise ValueError("must have at least 5 characters")
        return v

    class Config:
        orm_mode = True


class CustomerOut(CustomerBase):
    id: int
