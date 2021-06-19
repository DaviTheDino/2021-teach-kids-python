print("Thicc Mac Toes")
print("Commands: type in exit without quotation marks to exit the game. To place a circle or cross on the board, first type the row letter then the column number, e.g. A1, C3, etc...")
print("Thic Mac Toes")
print("  *******")
print("  |X|X|X|")
print("  |X|X|X|")
print("  |X|X|X|")
def Babocheckend(babo):
    if babo[0]==babo[1]==babo[2] or babo[3]==babo[4]==babo[5] or babo[6]==babo[7]==babo[8]or babo[1]==babo[4]==babo[7] or babo[2]==babo[5]==babo[8] or babo[0]==babo[4]==babo[8] or babo[2]==babo[4]==babo[8] or babo[0]==babo[3]==babo[6]:
        print("Babo is happy.You win!")
    else:
        print("It is a tie. Cat eye or cat foot or cat body i don't remember")
    exit()
def Babocheck(babo):
    if babo[0]==babo[1]==babo[2] or babo[3]==babo[4]==babo[5] or babo[6]==babo[7]==babo[8]or babo[1]==babo[4]==babo[7] or babo[2]==babo[5]==babo[8] or babo[0]==babo[4]==babo[8] or babo[2]==babo[4]==babo[8] or babo[0]==babo[3]==babo[6]:
        print("Babo is happy. You win!")
        exit()
def Babo(babo):
    print('\n')
    print('            +*****+')
    print('            |{}|{}|{}|'.format(babo[0],babo[1], babo[2]))
    print('            |{}|{}|{}|'.format(babo[3],babo[4], babo[5]))
    print('            |{}|{}|{}|'.format(babo[6],babo[7], babo[8]))
    print('            +*****+')
    print("\n")
babo=['1','2','3','4','5','6','7','8','9']
Babo(babo)
move=int(input("What square?"))
babo[move-1]="X"
Babo(babo)
Babocheck(babo)
move=int(input("What square player2?"))
babo[move-1]="O"
Babo(babo)
Babocheck(babo)
move=int(input("What square?"))
babo[move-1]="X"
Babo(babo)
Babocheck(babo)
move=int(input("What square player2?"))
babo[move-1]="O"
Babo(babo)
Babocheck(babo)
move=int(input("What square?"))
babo[move-1]="X"
Babo(babo)
Babocheck(babo)
move=int(input("What square player2?"))
babo[move-1]="O"
Babo(babo)
Babocheck(babo)
move=int(input("What square?"))
babo[move-1]="X"
Babo(babo)
Babocheck(babo)
move=int(input("What square player2?"))
babo[move-1]="O"
Babo(babo)
Babocheck(babo)
move=int(input("What square?"))
babo[move-1]="X"
Babo(babo)
Babocheck(babo)