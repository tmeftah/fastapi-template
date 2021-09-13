from typing import List
from fastapi import APIRouter, Depends

from app.api.controllers.products import get_all_products, create_new_product
from app.schemas import products as ProductSchema


router = APIRouter()


@router.get("/",response_model=List[ProductSchema.ItemBase])
def get_all(controller=Depends(get_all_products)):    
    return controller

@router.post("/2")
def get_all2(controller=Depends(create_new_product)):    
    return controller