from typing import Dict
from pydantic import BaseModel


class fraseInDB(BaseModel):
    nombreFrase: str
    frase: str


database_frases = Dict[str, fraseInDB]


def create_frase(frase_in_db: fraseInDB):
    database_frases[frase_in_db.nombreFrase] = frase_in_db
    return frase_in_db


database_frases = {
    "frase1": fraseInDB(**{"nombreFrase": "camilo24",
                           "frase": "root"}),
    "frase2": fraseInDB(**{"nombreFrase": "andres18",
                           "frase": "hola"}),
}
