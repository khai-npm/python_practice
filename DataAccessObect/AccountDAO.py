import sys
sys.path.append('./BusinessObject/')
sys.path.append('./Util/')
from Account import Account
from HashPasswordUtil import HashPassword
from RoleDefinitionUtil import RoleDefine


class AccountDAO:
    list : Account = []
    Role : str = []
    hash = HashPassword()
    

    def __init__(self):
        self.Role.append("Undefined")
        self.Role.append("Admin")
        self.Role.append("User")

        self.list : Account = []
        self.list.append(Account(UserID=0,
                                 UserName="admin",
                                 Password=self.hash.DoHashPassword("1"),
                                 Fullname="Admin Admin",
                                 PhoneNumber="0000000000",
                                 descripition="day la tai khoan admin",
                                 RoleID=self.Role[1]))
        
        self.list.append(Account(UserID=1,
                                 UserName="khai",
                                 Password=self.hash.DoHashPassword("123"),
                                 Fullname="Khai Nguyen",
                                 PhoneNumber="0123456789",
                                 descripition="tai khoan cua toi",
                                 RoleID=self.Role[2]))
        
        self.list.append(Account(UserID=2,
                                 UserName="Minh",
                                 Password=self.hash.DoHashPassword("1234"),
                                 Fullname="Minh Truong",
                                 PhoneNumber="0988553321",
                                 descripition="day la tai khoan admin",
                                 RoleID=self.Role[2]))
        
    def getAllRole(self):
        index = 0
        for i in self.Role:
            print("["+str(index)+"]: " + i)
            index = index + 1

    def getList(self):
        i : Account
        for i in self.list:
            print("[UID:"+ str(i.UserID) +"]: "+ i.UserName +" (Role: '" + i.RoleID + "')")

    def GenerateUID(self):
        return len(self.list)
    
    def AddnewRole(self, newRole):
        self.Role.append(newRole)
    
    def AddAccount(self, UserName, Password, ConfirmPassword):
        hash = HashPassword()
        NUID = int(self.GenerateUID())
        try:
            if " " in UserName or " " in Password:
                UserName = UserName.replace(" ","")
                Password = Password.replace(" ","")
            
            if UserName == "" or Password == "":
                raise ValueError('Username or Password must not be null')
            for i in self.list:
                if i.UserName.lower() == UserName.lower():
                    raise ValueError('already exist username !')
            
                if Password != ConfirmPassword.replace(" ",""):
                    raise ValueError('Password and Confirmination does not match !')
            
            self.list.append(Account(UserID=NUID, 
                                     UserName=UserName,
                                       Password=self.hash.DoHashPassword(Password),
                                       RoleID=self.Role[2], Fullname="null",
                                       PhoneNumber="null",
                                       descripition="null"))
            print("account:", UserName, "registered successfully!")
        except ValueError as e:
            print("Register failed ! reason: " , e)

    def CheckLogin(self, UserName, Password):
        try:
            if " " in UserName or " " in Password:
                raise ValueError('Username or Password must not have space')

            tempHash = self.hash.DoHashPassword(Password)
            check = False
            for i in self.list:
                if i.UserName.lower() == UserName.lower():
                    if i.Password == tempHash:
                        print("account:["+UserName+"]verified Successfully !")
                        check = True

            if check is False:
                raise ValueError('Verficiation failed ! Username or Password does not match')
        except ValueError as e:
            print("Verficiation failed ! reason: " , e)
        return check
                    
    def SearchByKeyword(self, keyword):
        result : Account = []
        for i in self.list:
            if keyword.lower().strip() in i.UserName.lower().strip() or keyword.lower().strip() in i.PhoneNumber or keyword.lower().strip() in i.Fullname or keyword.lower().strip() in i.descripition:
                result.append(i)

        for i2 in result:
            print("------["+ i2.Fullname +"]------")
            print("[UID:"+ str(i2.UserID) +"]: "+ i2.UserName +" (Role: '" + i2.RoleID + "')")
            print("phone number: " + i2.PhoneNumber)
            print("descripition: " + i2.descripition)
            print("-------------")
    def ViewAccountDetail(self, session):
        result : Account
        for i in self.list:
            if session.lower() == i.UserName.lower():
                result = i
        if result is None:
            print("Error, data is missing !")
        else:
            print("-----[" + result.UserName+"]-----")
            print("UID:", result.UserID)
            print("Full Name:",result.Fullname)
            print("Phone Number:",result.PhoneNumber)
            print("")
            print("descripition: ", result.descripition)

            print("Role: ",result.RoleID )
            print("--------------------------------")


            return result
        
    def GetAccountDetail(self, session):
        result : Account
        for i in self.list:
            if session.lower() == i.UserName.lower():
                result = i
        if result is None:
            print("Error, data is missing !")
        else:



            return result
        


    def GetSessionRole(self, session):
        result : Account
        for i in self.list:
            if session.lower() in i.UserName.lower():
                result = i.RoleID
        if result is None:
            print("Error, data is missing !")
        
        return result
    

    def UpdateAccountInfoMode(self, session ,fullname, PhoneNumber, descripition):
        i : Account
        for i in self.list:
            if session.lower() == i.UserName.lower():
                i.Fullname = fullname
                i.PhoneNumber = PhoneNumber
                i.descripition = descripition

    def UpdateAccountPasswordMode(self, session ,Password):
        i : Account
        for i in self.list:
            if session.lower() == i.UserName.lower():
                i.Password = self.hash.DoHashPassword(Password)

    def UpdateAccountRoleMode(self, session ,RoleID):
        i : Account
        for i in self.list:
            if session.lower() == i.UserName.lower():
                i.RoleID = self.Role[RoleID]


    
#Test run :
'''          
session = AccountDAO()
print("before")
print("--------------------")
session.getList()
print("--------------------")
session.AddAccount("admin", "123", "123")
session.AddAccount("bodanh123", "123", "1234")
session.AddAccount("bodanh123", "1234", "1234")

print("after")
print("--------------------")
session.getList()
print("--------------------")

session.CheckLogin("Khai","123")
session.CheckLogin("admin","1")
session.CheckLogin("admin","w")
session.CheckLogin("admwin","1")
    '''