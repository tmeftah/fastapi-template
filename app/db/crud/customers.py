from sqlalchemy.orm import Session
from app.db.models.customers import Customer
from app.schemas import customers as CustomerSchema


def get_all(db: Session):
    res = db.query(Customer).pagination()
    return res


def get_by_id(id: int, db: Session):
    return db.query(Customer).filter(Customer.id == id).first()


def get_by_name(name: str, db: Session):
    return db.query(Customer).filter(Customer.name == name).first()


def add(customer: CustomerSchema.CustomerBase, db: Session):
    new = Customer(**customer.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new
