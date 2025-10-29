from pydantic import BaseModel

class GeneCreate(BaseModel):
    gene: str
    type: str
    alteration: str
    alt_type: str

class GeneResponse(BaseModel):
    id: int
    gene: str
    type: str
    alteration: str
    alt_type: str

    class Config:
        orm_mode = True