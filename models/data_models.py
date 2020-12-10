
from pydantic import BaseModel

class DataIn(BaseModel):
    nombreGasto: str
    valor: int

class DataOut(BaseModel):
    nombreGasto: str
    valor: int