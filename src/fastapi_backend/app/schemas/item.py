from pydantic import BaseModel

class ItemCreate(BaseModel):
    title:str

class ItemResponse(BaseModel):
    id:int
    title:str

    class Config:
        from_attributes=True