
from pydantic import BaseModel



class BLOG(BaseModel):
    title : str
    body : str
