from sqlalchemy.orm import Session
from app.db.models.suppliers import Supplier


def get_all(db: Session):
    res = db.query(Supplier).pagination()

    return res


def get_by_id(id: int, db: Session):
    return db.query(Supplier).filter(Supplier.id == id).first()


def get_by_name(name: str, db: Session):
    return db.query(Supplier).filter(Supplier.name == name).first()


def add(name: str, db: Session):
    _exist = db.query(Supplier).filter(Supplier.name == name).first()
    return _exist
