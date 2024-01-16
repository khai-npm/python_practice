import sys
sys.path.append('./BusinessObject/')
sys.path.append('./Util/')
from Role import Role

class RoleDAO:
    roleList : Role = []
    def __init__(self):
        self.roleList.append(Role(RoleID=1, RoleName="Admin", RolePermission=["All", "*"]))
        self.roleList.append(Role(RoleID=0, RoleName="Undefined", RolePermission=[""]))
        self.roleList.append(Role(RoleID=2, RoleName="User", RolePermission=[""]))

        
    def AddnewRole(self, rolename, permission=[]):
        self.roleList.append(Role(RoleID=len(self.roleList), RoleName=rolename, RolePermission=permission))


    def checkRoleReturnPermission(self, roleName):
        role : Role
        for i in self.roleList:
            if roleName == i.RoleName:
                permission = i.RolePermission
        

        return permission
