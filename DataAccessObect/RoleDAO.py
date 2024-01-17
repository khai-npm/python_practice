import sys
sys.path.append('./BusinessObject/')
sys.path.append('./Util/')
from Role import Role

class RoleDAO:
    roleList : Role = []
    def __init__(self):
        self.roleList.append(Role(RoleID=1, RoleName="Admin", RolePermission=["All"]))
        self.roleList.append(Role(RoleID=0, RoleName="Undefined", RolePermission=[""]))
        self.roleList.append(Role(RoleID=2, RoleName="User", RolePermission=[""]))

    def ViewRoleDetai(self, roleName):
        i : Role
        for i in self.roleList:
            if i.RoleName == roleName:
                print("role ID: " + str(i.RoleID))
                print("Role Name: " + i.RoleName)
                print("role Perrmission: ", i.RolePermission)

    def UpdateRolePermission(self, roleName, Perrmission):
        i : Role
        for i in self.roleList:
            if roleName == i.RoleName:
                i.RolePermission = Perrmission
        
    def AddnewRole(self, rolename, permission=[]):
        try:
            for i in self.roleList:
                if rolename == i.RoleName:
                    raise ValueError("existed role!")
            self.roleList.append(Role(RoleID=len(self.roleList), RoleName=rolename, RolePermission=permission))
        except ValueError as e:
            print("Error adding new role:" + str(e))

    def checkRoleReturnPermission(self, roleName):
        role : Role
        for i in self.roleList:
            if roleName == i.RoleName:
                permission = i.RolePermission
        

        return permission
