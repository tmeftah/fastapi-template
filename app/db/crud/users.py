from sqlalchemy.orm import Session
from app.db.models.users import User
from app.middlewares.auth import auth


def get_all(db: Session):
    return db.query(User).all()


def get_by_name(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user


def get_by_id(
    username: int,
    db: Session,
):
    user = db.query(User).filter(User.id == username).first()

    return user


def add(username: str, password: str, db: Session):
    user = User(username=username, hashed_password=auth.get_password_hash(password))

    db.add(user)
    db.commit()

    return {"id": user.id, "username": user.username, "hashed_password": user.hashed_password}
