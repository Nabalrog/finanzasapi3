
from pydantic import BaseModel


class FraseIn(BaseModel):
    nombreFrase: str
    frase: str
