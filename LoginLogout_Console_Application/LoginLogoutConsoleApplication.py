import time
import os
import sys
sys.path.append('./Util/')
from MenuUtil import menu

sys.path.append('./DataAccessObect')
from AccountDAO import AccountDAO

SessionDB = AccountDAO()
Session = "null"


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

    if Session != "null":
        os.system('cls')
        print("-=welcome user:["+Session+"]=-")
        newMenu2 = menu()
        newMenu2.AddChoice("view list of all account ")
        newMenu2.AddChoice("View Account Detail")
        newMenu2.AddChoice("search account")
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
                print("--------==[Account detail]==----------")
                SessionDB.ViewAccountDetail(Session)
                print("--------------------------------------")

                print()
                print("press enter to continue....")
                temp = input()
                temp = None


            case 3:
                os.system('cls')
                print("enter keyword: ")
                Ipkeyword = str(input())

                print("---------=[Result]=--------")

                print(SessionDB.SearchByKeyword(Ipkeyword))
                print("---------------------------")

                print()
                print("press enter to continue....")
                temp = input()
                temp = None


            case 4:
                os.system('cls')
                Session = "null"
            case 5:
                os.system('cls')
                repeat_flag = False 

