from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.crud import customers as crud
from app.schemas import customers as CustomerSchema
from app.db.database import get_db


def get_all_customers(db: Session = Depends(get_db)):

    return crud.get_all(db)


def create_new_customer(customer: CustomerSchema.CustomerBase, db: Session = Depends(get_db)):
    if crud.get_by_name(customer.name, db=db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"customer {customer.name} all ready exists!!!",
        )
    return crud.add(customer, db=db)
