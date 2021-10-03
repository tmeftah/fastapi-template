from sqlalchemy import Column, Integer, String
from app.db.database import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)
    postcode = Column(String)
    town = Column(String)
    salutation = Column(String)
    phone = Column(String)
    fax = Column(String)
    website = Column(String)
    Remarks = Column(String)
