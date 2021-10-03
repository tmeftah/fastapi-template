from pydantic import BaseModel


class SupplierBase(BaseModel):
    id: int
    name: str
    address: str
    postcode: str
    town: str
    salutation: str
    phone: str
    fax: str
    website: str
    Remarks: str

    class Config:
        orm_mode = True
