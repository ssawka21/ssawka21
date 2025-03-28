from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    quantity: int
