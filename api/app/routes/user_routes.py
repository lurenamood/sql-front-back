# api/app/routes/user_routes.py

from fastapi import APIRouter, Body, status
from app.crud import user_crud
from app.schemas.user_schema import UserUpdate
from app.crud.user_crud import set_user_inactive

router = APIRouter()


@router.get("/usuarios", tags=["Users"])
def read_users():
    return user_crud.get_users()


@router.post("/create_user", status_code=status.HTTP_201_CREATED, tags=["Users"])
def create_user(user: dict = Body(...)):
    return user_crud.create_user(user)


@router.get("/filteremail", tags=["Users"])
def get_by_email(domain: str):
    return user_crud.get_users_by_email_domain(domain)



@router.put("/update_state", status_code=status.HTTP_200_OK, tags=["Users"])
def update_user(user: UserUpdate):
    return user_crud.update_user_fields(user)


@router.delete("/{user_id}", tags=["Users"])
def delete_user(user_id: int):
    return set_user_inactive(user_id)
