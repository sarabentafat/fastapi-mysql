from fastapi import APIRouter
from db.database import *
from models.models import users
from schemas.schemas import User

user = APIRouter()

@user.post("/users", response_model=User)
def create_user(user: User):
    new_user = {
        "username": user.username, 
        "display_name": user.display_name,
        "year_of_birth": user.year_of_birth
    }
    result = db.execute(users.insert().values(new_user))
    return db.execute(users.select().where(users.c.id == result.lastrowid)).first()

@user.get("/users", response_model=list[User])
def get_all_users():
    return db.execute(users.select()).fetchall()

@user.get("/users/{id}", response_model=User,)
def get_user(id: int):
    return db.execute(users.select().where(users.c.id == id)).first()

@user.put("/users/{id}", response_model=User)
def update_user(user: User, id: int):
    db.execute(
        users.update()
        .values(username=user.username, display_name=user.display_name, year_of_birth=user.year_of_birth)
        .where(users.c.id == id)
    )
    return db.execute(users.select().where(users.c.id == id)).first()

@user.delete("/users/{id}")
def delete_user(id: int):
    db.execute(users.delete().where(users.c.id == id))
    return db.execute(users.select().where(users.c.id == id)).first()
