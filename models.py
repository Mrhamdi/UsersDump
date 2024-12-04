from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str


class RegRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str

class Delete(BaseModel):
    id:str

class Update(BaseModel):
    id:str
    first_name: str
    last_name: str
    password: str