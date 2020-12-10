from typing import Dict
from pydantic import BaseModel

class DataInDB(BaseModel):
    nombreGasto: str
    valor: int


database_data = Dict[str, DataInDB]


def get_data(nombre_Gasto: str, valor: int):
    if nombre_Gasto in database_data.keys():
        return database_data[nombre_Gasto, valor]
    else:
        return None


def crear_data(creardata_in_db: DataInDB):
    database_data[creardata_in_db.nombre_Gasto] = DataInDB
    database_data[creardata_in_db.valor] = DataInDB
    return DataInDB


database_data = {
    "Gasto1": DataInDB(**{"Nombre gasto": "peluqueria", "valor": 5000}),

}
