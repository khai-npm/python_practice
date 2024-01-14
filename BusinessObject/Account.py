from pydantic import BaseModel
class Account(BaseModel):
    UserName : str
    Password : bytes







'''  
    #constructor

    def __init__(self):
        self.UserName = ""
        self.Password = ""

    def SetInfo(self, UserName, Password):
        self.UserName = UserName
        self.Password = Password

    #getter (note: object.Get có giá trị trả về là địa chỉ vùng nhớ cấp phát của hàm, object.Get() mới lấy giá trị trả về của hàm)
    def GetUserName(self):
        return self.UserName
    def GetPassword(self):
        return self.Password
    
    #setter
    def SetUserName(self, newUserName):
        self.UserName = newUserName
    def SetPassword(self, newPassword):
        self.Password = newPassword  

    def toString(self):
        return str("Account: ['Username': '"+ self.GetUserName() +"', 'Password': '"+ self.GetPassword +"']")
        

print(a.UserName)
print(a.Password)

=> admin , 1

print(a.GetUserName)
print(a.GetPassword)

=>  0x000001CC1F5DE300,  0x000001CC1F5DE300


a = Account()
a.SetInfo("admin","1")
print(a.GetUserName())
print(a.GetPassword())

a.toString()

'''
