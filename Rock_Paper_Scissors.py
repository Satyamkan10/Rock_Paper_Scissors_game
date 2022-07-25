#from http.client import CONTINUE
import random
while True:
    player=int(input("enter the n.o to select (0=Rock , 1=Scissors, 2=Paper) "))
    comp=random.randint(0,3)
    if (player==0 and comp==0):
        print("DRAW")
    elif(player==1 and comp==1):
        print("DRAW")
    elif(player==2 and comp==2):
        print("DRAW")
    elif(player==0 and comp==1):
        print("you win")
    elif(player==0 and comp==2):
        print("you loose")
    elif(player==1 and comp==0):
        print("you loose")
    elif(player==1 and comp==2):
        print("you win")
    elif(player==2 and comp==0):
        print("you loose")
    elif(player==2 and comp==1):
        print("you win")
    CONTINUE=int(input("ENTER TO CONTINUE")) #press 0 exit game or press 1 to continue
    if (CONTINUE==0):
        break
    else:
        continue