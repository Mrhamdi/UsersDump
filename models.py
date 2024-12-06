from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str
    key:str

class masterUsers(BaseModel):
    key:str

class RegRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    password: str
    key:str

class masterRegister(BaseModel):
    username:str
    password:str
    key:str


class Delete(BaseModel):
    id:str
    key:str

class Update(BaseModel):
    id:str
    first_name: str
    last_name: str
    password: str
    key:str