from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    username: str
    display_name: str
    year_of_birth: int