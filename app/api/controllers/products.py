from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.crud import products as crud
from app.db.database import get_db


def get_all_products(db: Session = Depends(get_db)):

    return crud.get_all(db)


def create_new_product(title: str, db: Session = Depends(get_db)):
    if crud.get_by_title(title, db):
        return "nok"
    return crud.add(title)
