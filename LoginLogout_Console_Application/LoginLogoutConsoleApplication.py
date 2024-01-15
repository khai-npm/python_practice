import time
import os
import sys
sys.path.append('./Util/')
from MenuUtil import menu
from RoleDefinitionUtil import RoleDefine
from HashPasswordUtil import HashPassword

sys.path.append('./DataAccessObect')
from AccountDAO import AccountDAO

SessionDB = AccountDAO()
Session = "null"
SessionRole = SessionDB.Role[0]


repeat_flag = True
while repeat_flag is True:


    if Session == "null":
        os.system('cls')
        newMenu = menu()
        newMenu.AddChoice("Login ")
        newMenu.AddChoice("Register Account")
        UserChoiceResult = newMenu.PrintChoice()
        print("user choice is ", UserChoiceResult)

        match UserChoiceResult:
            case 1:
                os.system('cls')
                print("enter UserName:")
                IpUserName = str(input())
                print("enter Password:")
                IpPassword = str(input())

                if (SessionDB.CheckLogin(IpUserName, IpPassword) is  True):
                    Session = IpUserName
                    SessionRole = SessionDB.GetSessionRole(IpUserName)

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            case 2:
                os.system('cls')
                print("enter new UserName:")
                IpNUserName = str(input())
                print("enter new Password:")
                IpNPassword = str(input())
                print("Password Confirmation:")
                RPassword = str(input())

                SessionDB.AddAccount(IpNUserName, IpNPassword, RPassword)

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            case 3:
                os.system('cls')
                repeat_flag = False   


# Admin Menu


    if Session != "null" and SessionRole == "Admin":
        os.system('cls')
        print("-=Administrator:["+Session+"]=-")
        newMenu2 = menu()
        newMenu2.AddChoice("view list of all account ")
        newMenu2.AddChoice("View Account Detail")
        newMenu2.AddChoice("View designated Account Detail")
        newMenu2.AddChoice("update your account's info ")
        newMenu2.AddChoice("update designated account's info ")
        newMenu2.AddChoice("search account")
        newMenu2.AddChoice("view role list")
        newMenu2.AddChoice("add new role")
        newMenu2.AddChoice("Log out")
        UserChoiceResult = newMenu2.PrintChoice()
        print("user choice is ", UserChoiceResult)

        match UserChoiceResult:
            case 1:
                os.system('cls')
                SessionDB.getList()
                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            case 2:
                os.system('cls')
                SessionDB.ViewAccountDetail(Session)

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            
            case 3:
                os.system('cls')
                print("Input UserName of Account:")
                account = str(input())
                SessionDB.ViewAccountDetail(account)
                print()
                print("press enter to continue....")
                temp = input()
                temp = None



            case 4:
                updateFlag = True
                try:
                    while updateFlag is True:
                        os.system('cls')
                        print("[1] Update Account's infomation (phone, name, descripition,..)")
                        print("[2] Update Password")
                        UpdateChoice = int(input())
                        if int(UpdateChoice) != 1 and int(UpdateChoice) != 2:
                            raise ValueError('please input right number')
                        else:
                            match UpdateChoice:
                                case 1:
                                    print("enter your FullName:")
                                    fullname = input()

                                    print("enter your phone number:")
                                    phone = int(input())

                                    print("enter your descripition:")
                                    descripition = input()

                                    os.system('cls')
                                    print("confirm your account's password:")
                                    checkPass = input()

                                    sessionAcc = SessionDB.GetAccountDetail(Session)
                                    if SessionDB.hash.DoHashPassword(checkPass) == sessionAcc.Password:
                                        SessionDB.UpdateAccountInfoMode( session=Session,
                                                                        fullname=fullname, 
                                                                        PhoneNumber=phone,
                                                                        descripition=descripition)
                                        print("profile updated successfully !")
                                        updateFlag = False

                                    else:
                                        raise ValueError('Password authenication failed !')

                                case 2:
                                    print("confirm your account's old password:")
                                    checkPass = input()

                                    sessionAcc = SessionDB.GetAccountDetail(Session)
                                    if SessionDB.hash.DoHashPassword(checkPass) == sessionAcc.Password:
                                        print("enter your new password:")
                                        newPass = input()

                                        if SessionDB.hash.DoHashPassword(newPass) == sessionAcc.Password:
                                            raise ValueError('new password must not the same with old password !')

                                        print("confirm your new password:")
                                        newPassConfirm = input()

                                        if newPass == newPassConfirm:
                                            SessionDB.UpdateAccountPasswordMode(Session, newPass)
                                            print("updated password successfully !")
                                            updateFlag = False
                                            Session = "null"
                                            SessionRole = SessionDB.Role[0]

                                        else:
                                            raise ValueError('Password confirmation does not match!')

                                    else:
                                        raise ValueError('Password authenication failed !')
                except ValueError as e:
                    print("Update Failed ! reason:>",str(e))

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            
            case 5:
                os.system('cls')
                print("Input UserName of Account:")
                account = str(input())
                FoundAccount = SessionDB.GetAccountDetail(account)
                try:
                    if FoundAccount.UserName == Session:
                        
                        raise ValueError('you cannot update yourself though this function')
                    
                    print("[1] Update Account's infomation (phone, name, descripition,..)")
                    print("[2] Update Role")
                    UpdateChoice = int(input())
                    if int(UpdateChoice) != 1 and int(UpdateChoice) != 2:
                        raise ValueError('please input right number')
                    else:
                            match UpdateChoice:
                                case 1:
                                    print("enter new FullName:")
                                    fullname = input()

                                    print("enter new phone number:")
                                    phone = int(input())

                                    print("enter new descripition:")
                                    descripition = input()

                                    
                                    SessionDB.UpdateAccountInfoMode( session=FoundAccount.UserName,
                                                                        fullname=fullname, 
                                                                        PhoneNumber=phone,
                                                                        descripition=descripition)
                                    print("profile updated successfully !")
                                    updateFlag = False


                                case 2:
                                    chooseRole = True
                                    while chooseRole is True:
                                        SessionDB.getAllRole()
                                        print("------------")
                                        print(" sign new Role based on number which is displaying on screen: ")
                                        roleChoice = int(input())
                                        if roleChoice<0 or roleChoice > len(SessionDB.Role)-1:
                                            raise ValueError('please type correct number')
                                        else:
                                            chooseRole = False
                                            SessionDB.UpdateAccountRoleMode(FoundAccount.UserName, roleChoice)
                                            print("update role successfully !")
                                            


                except ValueError as e:
                    print("Update failed ! reason:", str(e))

                print()
                print("press enter to continue....")
                temp = input()
                temp = None


            case 6:
                os.system('cls')
                print("enter keyword: ")
                Ipkeyword = str(input())

                print("---------=[Result]=--------")

                SessionDB.SearchByKeyword(Ipkeyword)
                print("---------------------------")

                print()
                print("press enter to continue....")
                temp = input()
                temp = None

            case 7:
                os.system('cls')
                SessionDB.getAllRole()
                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            case 8:
                os.system('cls')
                print("input new role: ")
                newRole = input()
                SessionDB.AddnewRole(newRole)

                print()
                print("press enter to continue....")
                temp = input()
                temp = None


            case 9:
                os.system('cls')
                Session = "null"
                SessionRole = SessionDB.Role[0]
            case 10:
                os.system('cls')
                repeat_flag = False 

# User Menu

    if Session != "null" and SessionRole != "Admin":
        os.system('cls')
        print("-=Welcome User:["+Session+"]=-")
        newMenu2 = menu()
        newMenu2.AddChoice("View Account Detail")
        newMenu2.AddChoice("update your account's info ")
        newMenu2.AddChoice("Log out")
        UserChoiceResult = newMenu2.PrintChoice()
        print("user choice is ", UserChoiceResult)

        match UserChoiceResult:
            case 1:
                os.system('cls')
                SessionDB.ViewAccountDetail(Session)

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
           
            case 2:
                
                updateFlag = True
                try:
                    while updateFlag is True:
                        os.system('cls')
                        print("[1] Update Account's infomation (phone, name, descripition,..)")
                        print("[2] Update Password")
                        UpdateChoice = int(input())
                        if int(UpdateChoice) != 1 and int(UpdateChoice) != 2:
                            raise ValueError('please input right number')
                        else:
                            match UpdateChoice:
                                case 1:
                                    print("enter your FullName:")
                                    fullname = input()

                                    print("enter your phone number:")
                                    phone = int(input())

                                    print("enter your descripition:")
                                    descripition = input()

                                    os.system('cls')
                                    print("confirm your account's password:")
                                    checkPass = input()

                                    sessionAcc = SessionDB.GetAccountDetail(Session)
                                    if SessionDB.hash.DoHashPassword(checkPass) == sessionAcc.Password:
                                        SessionDB.UpdateAccountInfoMode( session=Session,
                                                                        fullname=fullname, 
                                                                        PhoneNumber=phone,
                                                                        descripition=descripition)
                                        print("profile updated successfully !")
                                        updateFlag = False

                                    else:
                                        raise ValueError('Password authenication failed !')

                                case 2:
                                    print("confirm your account's old password:")
                                    checkPass = input()

                                    sessionAcc = SessionDB.GetAccountDetail(Session)
                                    if SessionDB.hash.DoHashPassword(checkPass) == sessionAcc.Password:
                                        print("enter your new password:")
                                        newPass = input()

                                        if SessionDB.hash.DoHashPassword(newPass) == sessionAcc.Password:
                                            raise ValueError('new password must not the same with old password !')

                                        print("confirm your new password:")
                                        newPassConfirm = input()

                                        if newPass == newPassConfirm:
                                            SessionDB.UpdateAccountPasswordMode(Session, newPass)
                                            print("updated password successfully !")
                                            updateFlag = False
                                            Session = "null"
                                            SessionRole = SessionDB.Role[0]

                                        else:
                                            raise ValueError('Password confirmation does not match!')

                                    else:
                                        raise ValueError('Password authenication failed !')
                except ValueError as e:
                    print("Update Failed ! reason:>",str(e))

                print()
                print("press enter to continue....")
                temp = input()
                temp = None

            case 3:
                os.system('cls')
                Session = "null"
                SessionRole = SessionDB.Role[0]
            case 4:
                os.system('cls')
                repeat_flag = False

