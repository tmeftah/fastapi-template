from fastapi import APIRouter, Depends
from app.api.controllers import users
from app.schemas import users as users_schema


router = APIRouter()


@router.post("/create")
def create_user(controller=Depends(users.create_new_user)):
    return controller


@router.post("/token", response_model=users_schema.Token)
def login_for_access_token(controller=Depends(users.authenticate_user)):
    return controller


@router.get("/")
def get_all(controller=Depends(users.get_all_users)):
    return controller


@router.get("/{id}", response_model=users_schema.User)
def get_on_id(controller: users = Depends(users.get_user_on_id)):
    return controller
