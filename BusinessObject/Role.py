from pydantic import BaseModel

class Role(BaseModel):
    RoleID : int
    RoleName : str
    RolePermission : list = []