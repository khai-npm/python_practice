import time
import os
import sys
sys.path.append('./Util/')
from MenuUtil import menu
from RoleDefinitionUtil import RoleDefine
from HashPasswordUtil import HashPassword

sys.path.append('./DataAccessObect')
from AccountDAO import AccountDAO
from RoleDAO import RoleDAO

SessionDB = AccountDAO()
Session = "null"
SessionRole = SessionDB.Role[0]
SessionRoleDB = RoleDAO()
PermissionSessionList = []
RolePermission : int

repeat_flag = True
while repeat_flag is True:
    RolePermission = int(SessionDB.Role.index(SessionRole))
    PermissionSessionList = SessionRoleDB.checkRoleReturnPermission(SessionRole)

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
                    RolePermission = int(SessionDB.Role.index(SessionRole))
                    PermissionSessionList = SessionRoleDB.checkRoleReturnPermission(SessionRole)

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
    if Session != "null" and SessionRole == "Undefined":
        os.system('cls')
        print("this account does not have permission to access")
        print()
        print("press enter to continue....")
        temp = input()
        temp = None
        os.system('cls')
        Session = "null"
        SessionRole = SessionDB.Role[0]
    
    if SessionRole != "null" and SessionRole != "Undefined":
        os.system("cls")

        newMenuPer = menu()
        newMenuPer.AddChoice("View Your Account Detail")
        newMenuPer.AddChoice("update your account's info ")
        if "All" in PermissionSessionList or "ViewAcc" in PermissionSessionList:
            newMenuPer.AddChoice("view list of all account")
            newMenuPer.AddChoice("View designated Account Detail")
            newMenuPer.AddChoice("search account")
        else:
            
            newMenuPer.AddChoice("-")
            newMenuPer.AddChoice("-")
            newMenuPer.AddChoice("-")

        if "All" in PermissionSessionList or "EditAcc" in PermissionSessionList:
            newMenuPer.AddChoice("update designated account's info ")
        else:
            newMenuPer.AddChoice("-")

        if "All" in PermissionSessionList or "ViewRole" in PermissionSessionList:
            newMenuPer.AddChoice("view role list")
        else:
            newMenuPer.AddChoice("-")

        if "All" in PermissionSessionList or "EditRole" in PermissionSessionList: 
            newMenuPer.AddChoice("add new role")
        else:
            newMenuPer.AddChoice("-")

        newMenuPer.AddChoice("Log out")
        UserChoiceResult = newMenuPer.PrintChoice()
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
                                    phone = "0"+int(input())

                                    print("enter your descripition:")
                                    descripition = input()
                                    if fullname == "" or phone == "" or descripition == "":
                                        raise ValueError('infomation field must not be null')
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

                if "All" not in PermissionSessionList and "ViewAcc" not in PermissionSessionList:
                    os.system('cls')
                    print("Not supported yet!")
                else:
                    os.system('cls')
                    SessionDB.getList()
                    

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
                
                

            case 4:
                if "All" not in PermissionSessionList and "ViewAcc" not in PermissionSessionList:
                    os.system('cls')
                    print("Not supported yet!")
                else:
                    try:
                        os.system('cls')
                        SessionDB.getList()
                        print("choose an account to view")
                        choice = int(input())
                        if choice < 0 or choice > len(SessionDB.list)-1:
                            raise ValueError('account id not exist to view')
                    except ValueError as e:
                        print("Error: "+str(e))
                    SessionDB.ViewAccountDetail(SessionDB.list[choice].UserName)
                    

                print()
                print("press enter to continue....")
                temp = input()
                temp = None

            case 6:
                if "All" not in PermissionSessionList and "EditAcc" not in PermissionSessionList:
                    os.system('cls')
                    print("Not supported yet!")
                else:
                    try:
                        os.system('cls')
                        SessionDB.getList()
                        print("choose an account to view")
                        choice = int(input())
                        if choice < 0 or choice > len(SessionDB.list)-1:
                            raise ValueError('account id not exist to update')
                        
                        result = SessionDB.list[choice]

                        if result.UserName == Session:
                        
                            raise ValueError('you cannot update yourself though this function')
                        os.system('cls')
                        print("[1] Update Account's infomation (phone, name, descripition,..)")
                        print("[2] Update Role")
                        UpdateChoice = int(input())
                        if int(UpdateChoice) != 1 and int(UpdateChoice) != 2:
                            raise ValueError('please input right number')
                        else:
                                match UpdateChoice:
                                    case 1:
                                        os.system('cls')
                                        print("enter new FullName:")
                                        fullname = input()

                                        print("enter new phone number:")
                                        phone = "0"+int(input())

                                        print("enter new descripition:")
                                        descripition = input()

                                        if fullname == "" or phone == "" or descripition == "":
                                            raise ValueError('infomation field must not be null')

                                    
                                        SessionDB.UpdateAccountInfoMode( session=SessionDB.list[choice].UserName,
                                                                        fullname=fullname, 
                                                                        PhoneNumber=phone,
                                                                        descripition=descripition)
                                        print("profile updated successfully !")
                                        updateFlag = False


                                    case 2:
                                        os.system('cls')
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
                                                SessionDB.UpdateAccountRoleMode(SessionDB.list[choice].UserName, roleChoice)
                                                print("update role successfully !")
                    
                    except ValueError as e:
                        print("Update failed ! reason:", str(e))

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
                    


            case 5:
                if  "All" not in PermissionSessionList and "ViewAcc" not in PermissionSessionList:
                    os.system('cls')
                    print("Not supported yet!")
                else:
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
                if "All" not in PermissionSessionList and "ViewRole" not in PermissionSessionList:
                    os.system('cls')
                    print("Not supported yet!")
                else:
                    os.system('cls')
                    SessionDB.getAllRole()
                    

                print()
                print("press enter to continue....")
                temp = input()
                temp = None
            case 8:
                if "All" not in PermissionSessionList and "EditRole" not in PermissionSessionList:
                    os.system('cls')
                    print("Not supported yet!")
                else:
                    os.system('cls')
                    print("input new role's name: ")
                    newRole = input()

                    os.system('cls')

                    print("All")
                    print("ViewAcc")
                    print("EditAcc")
                    print("ViewRole")
                    print("EditRole")
                    print("------------------------------")
                    print("add permission for this role, using ',' for multiple permission")
                    print(" -=note: 'All' is able to access all administator function=-")
                    print("Example: All, ViewAcc,... ")

                    IPpermission = input().replace(" ", "")
                    perList = IPpermission.split(",")

                    SessionDB.AddnewRole(newRole)
                    SessionRoleDB.AddnewRole(newRole, perList)
                    

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
'''
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
                                    phone = "0"+int(input())

                                    print("enter your descripition:")
                                    descripition = input()
                                    if fullname == "" or phone == "" or descripition == "":
                                        raise ValueError('infomation field must not be null')
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
                                    phone = input()

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
                                    phone = "0" + int(input())

                                    print("enter your descripition:")
                                    descripition = input()

                                    if fullname == "" or phone == "" or descripition == "":
                                        raise ValueError('infomation field must not be null')

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
'''

    