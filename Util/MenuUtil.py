import os
class menu:
    def __init__(self):
        self.MenuChoiceList = []

    def AddChoice(self, msg):
        self.MenuChoiceList.append(msg)

    def PrintChoice(self):
        exitFlag = False
        while exitFlag is False:
            indexNum=1
            print("-----------------------")
            for i in self.MenuChoiceList:
                print("["+ str(indexNum) +"]: "+i)
                indexNum = indexNum + 1
            print("["+str(indexNum)+"]: exit program")
            print("-----------------------")
            print("please input a number to choose your choice :")

            try:
                UserChoice = int(input())
                if UserChoice < 0 or UserChoice > indexNum:
                    raise ValueError()
                else:
                    exitFlag = True
                    return UserChoice

            except:
                print("ERROR: You must type correct number")
                print()
                print("press enter to continue....")
                temp = input()
                os.system('cls')
                temp = None
                exitFlag = False

            

#Test run :
'''
 
me = menu()
me.AddChoice("123321")
me.AddChoice("123321ww")
UCR = me.PrintChoice()
print("user choice is ", UCR)
'''


