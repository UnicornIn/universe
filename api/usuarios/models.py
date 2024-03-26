from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    full_name: str
    is_active: bool
