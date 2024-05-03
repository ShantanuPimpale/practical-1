import random

def PrintBoard(xState,oState):
    zero="X" if xState[0] else ("O" if oState[0] else 0)
    one="X" if xState[1] else ("O" if oState[1] else 1)
    two="X" if xState[2] else ("O" if oState[2] else 2)
    three="X" if xState[3] else ("O" if oState[3] else 3)
    four="X" if xState[4] else ("O" if oState[4] else 4)
    five="X" if xState[5] else ("O" if oState[5] else 5)
    six="X" if xState[6] else ("O" if oState[6] else 6)
    seven="X" if xState[7] else ("O" if oState[7] else 7)
    eight="X" if xState[8] else ("O" if oState[8] else 8)
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def sum(a,b,c):
    return a+b+c
def CheckWin(xState,oState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print("Hurray!!,X Won the Match!!")
            return 1
        if(sum(oState[win[0]],oState[win[1]],oState[win[2]])==3):
            print("Hurray!!,O Won the Match!!")
            return 0
    return -1
print("Welcome to Tic Tac Toe Game!!")
xState=[0,0,0,0,0,0,0,0,0]
oState=[0,0,0,0,0,0,0,0,0]
turn=1#turn of X
while(True):
    PrintBoard(xState,oState)
    if(turn==1):
        print("Chance Of X:")
        value=int(input("Please Enter the Number:"))
        xState[value]=1
    else:
        print("Computer's Chance:")
        value = random.randint(0,8)
        while xState[value] != oState[value]:
            value = random.randint(0, 8)
        oState[value] = 1
    cwin=CheckWin(xState,oState)
    if(cwin!=-1):
        PrintBoard(xState, oState)
        print("Match Over!!")
        break
    turn=1-turn
