from typing import Dict
from pydantic import BaseModel


class DataInDB(BaseModel):
    nombreGasto: str
    valor: int


database_data = Dict[str, DataInDB]


def get_data(nombreGasto: str):
    if nombreGasto in database_data.keys():
        return database_data[nombreGasto]
    else:
        return None


def crear_data(creardata_in_db: DataInDB):
    database_data[creardata_in_db.nombreGasto] = creardata_in_db
    database_data[creardata_in_db.valor] = creardata_in_db
    return creardata_in_db


database_data = {
    "Gasto1": DataInDB(**{"nombreGasto": "peluqueria", "valor": 5000}),

}
