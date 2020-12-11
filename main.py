
from db.user_db import get_user, create_user
from db.Data_db import get_data, crear_data
from models.user_models import UserIn, UserOut
from models.data_models import DataIn
from fastapi import FastAPI
from fastapi import HTTPException


api = FastAPI()


@api.get("/user/{username}")
async def obtain_user(usuariobuscado: UserOut):
    user_in_db = get_user(usuariobuscado.username)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    if user_in_db.password != usuariobuscado.password:
        return {"Autenticado": False}
    return {"hola:{user_in_db}"}


@api.post("/user/{username}")
async def postear_user(usuarioacrear: UserIn):
    new_User = create_user(usuarioacrear)
    if new_User == "":
        raise HTTPException(status_code=404, detail="No digito usuario ")
    return {"hola:{new_User}, bienvenido"}


@api.get("/DataOut/{nombreGasto}")
async def obtain_data(nombreGasto: str):
    nombreData_in_db = get_data(nombreGasto)
    if nombreData_in_db is None:
        raise HTTPException(status_code=404, detail="el gasto no existe")
    return nombreData_in_db


@api.post("/DataIn/")
async def postear_data(dataacrear: DataIn):
    new_data = crear_data(dataacrear)
    if new_data == "":
        raise HTTPException(status_code=404, detail="No creo gasto ")
    return new_data
