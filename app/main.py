from fastapi import FastAPI
from app.api.routes import api_router
from app.db import models
from app.db.database import engine, Base


Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(api_router, prefix="/v1")  # set the version number
