from typing import List
from fastapi import APIRouter, Depends
from app.api.controllers.customers import get_all_customers, create_new_customer
from app.schemas import customers as CustomerSchema


router = APIRouter()


@router.get("/", response_model=List[CustomerSchema.CustomerOut])
def get_all(controller=Depends(get_all_customers)):

    return controller


@router.post("/", response_model=CustomerSchema.CustomerOut)
def create(controller=Depends(create_new_customer)):

    return controller
