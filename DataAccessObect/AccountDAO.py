import sys
sys.path.append('./BusinessObject/')
sys.path.append('./Util/')
from Account import Account
from HashPasswordUtil import HashPassword


class AccountDAO:
    list : Account = []
    hash = HashPassword()
    

    def __init__(self):

        self.list : Account = []
        self.list.append(Account(UserName="admin", Password=self.hash.DoHashPassword("1")))
        self.list.append(Account(UserName="Khai", Password=self.hash.DoHashPassword("123")))
        self.list.append(Account(UserName="MinhTruong", Password=self.hash.DoHashPassword("321")))

    def getList(self):
        for i in self.list:
            print(i)
    
    def AddAccount(self, UserName, Password, ConfirmPassword):
        hash = HashPassword()
        try:
            if " " in UserName or " " in Password:
                raise ValueError('Username or Password must not have space')
            
            if UserName == "" or Password == "":
                raise ValueError('Username or Password must not be null')
            for i in self.list:
                if i.UserName.lower() == UserName.lower():
                    raise ValueError('already exist username !')
            
                if Password != ConfirmPassword:
                    raise ValueError('Password and Confirmination does not match !')
            
            self.list.append(Account(UserName=UserName, Password=self.hash.DoHashPassword(Password)))
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
            if keyword.lower() in i.UserName.lower():
                result.append(i)
        if len(result) == 0:
            print("Account with keyword: ["+keyword+"] not found")

        return result
    
    def ViewAccountDetail(self, session):
        result : Account
        for i in self.list:
            if session.lower() in i.UserName.lower():
                result = i
        if result is None:
            print("Error, data is missing !")
        else:
            print("UserName: " + result.UserName)
            print("Passsword: "+ "***")




    
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