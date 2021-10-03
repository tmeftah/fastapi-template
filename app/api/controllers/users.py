from fastapi import Depends, HTTPException, status
from fastapi.param_functions import Form
from sqlalchemy.orm import Session
from app.middlewares.auth import auth
from app.db.crud import users as crud
from app.db.database import get_db


class Form_token:
    def __init__(self, username: str = Form(...), password: str = Form(...)):
        self.username = username
        self.password = password


def authenticate_user(
    db: Session = Depends(get_db),
    form_data: Form_token = Depends(),
):
    user = crud.get_by_name(form_data.username, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if not auth.verify_password(
        plain_password=form_data.password, hash_password=user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return auth.create_access_token(user.id)


def get_all_users(user=Depends(auth.auth_wrapper), db: Session = Depends(get_db)):
    return crud.get_all(db)


def get_user_on_id(id: int, db: Session = Depends(get_db)):
    user = crud.get_by_id(id, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} was not found !!!"
        )

    return crud.get_by_id(id, db)


def create_new_user(username: str, password: str, db: Session = Depends(get_db)):
    return crud.add(username=username, password=password, db=db)
