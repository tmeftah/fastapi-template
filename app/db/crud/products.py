from sqlalchemy.orm import Session
from app.db.models.products import Item


def get_all(db: Session):
    res = db.query(Item).pagination()

    return res


def get_by_id(id: int, db: Session):
    return db.query(Item).filter(Item.id == id).first()


def get_by_title(title: str, db: Session):
    return db.query(Item).filter(Item.title == title).first()


def add(title: str, db: Session):
    _exist = db.query(Item).filter(Item.title == title).first()
    return _exist
