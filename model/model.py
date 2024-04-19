### ========== Import Library ========== ###
from pydantic import BaseModel

### ========== Define Blog Schema ========== ###
class Blog(BaseModel):
    title: str
    description: str
    content: str
    author: str