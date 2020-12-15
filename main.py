
from db.user_db import get_user, create_user
from db.Data_db import get_data, crear_data
from models.user_models import UserIn
from models.data_models import DataIn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
origins = ["http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
           "http://localhost", "http://localhost:8080",
           "http://127.0.0.1:8000",
           "http://127.0.0.1",
           ]

api = FastAPI()

api.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)


@api.get("/user/{username}")
async def obtain_user(username: str):
    user_in_db = get_user(username)
    if user_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    return {"hola:"+user_in_db.username}


@api.post("/user/")
async def postear_user(usuarioacrear: UserIn):
    new_User = create_user(usuarioacrear)
    if new_User == "":
        raise HTTPException(status_code=404, detail="No digito usuario ")
    return {"hola, bienvenido"}


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
