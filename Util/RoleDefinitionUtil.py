from pydantic import BaseModel

class RoleDefine(BaseModel):
    RoleID : int
    RoleName : str
    RolePermission : str = []