from fastapi import APIRouter

from .users import router as auth_router
from .products import router as products_router
from .projects import router as projects_router
from .customers import router as customers_router

api_router = APIRouter()  # create main router for all

# include all router with spec prefix and tag
api_router.include_router(auth_router, prefix="/users", tags=["users"])
api_router.include_router(products_router, prefix="/products", tags=["products"])
api_router.include_router(projects_router, prefix="/projects", tags=["projects"])
api_router.include_router(customers_router, prefix="/customers", tags=["customers"])
