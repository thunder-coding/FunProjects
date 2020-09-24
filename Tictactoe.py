''' Tic Tac Toe for 2 players in Python '''
# Made by :Pratham Prasoon, Yaksh Bariya
# Twitter @PrassonPratham , @CodingThunder
  
import sys
 
#Board   1. 2. 3. 4. 5. 6. 7. 8. 9.
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#Note :    0 -> Empty box
X = 1    # 1 -> X
O = 2    # 2 -> O


#Current Player = X
player = X

#Number of boxes that are filled
slotFilled = 0

def boxValue(boxNumber):
    if(board[boxNumber-1] == 1):
        return "X"
    elif(board[boxNumber-1] == 2):
        return "O"
    else:
        return " "


#Draw the Tic Tac Toe Board
def drawBoard():
    print("-------------") 
    print("| " + boxValue(1) + " | " + boxValue(2) + ' | '+ boxValue(3) + ' |')
    print("|-----------|" )
    print("| " + boxValue(4) + " | " + boxValue(5) + ' | '+ boxValue(6) + ' |' )
    print("|-----------|"  )
    print("| " + boxValue(7) + " | " + boxValue(8) + ' | '+ boxValue(9) + ' |')
    print("-------------" )
 
#Check if the game has been won or Tied 
def checkGameResult():
    if board[0]==board[1]==board[2]!=0 or board[3]==board[4]==board[5]!=0 or board[6]==board[7]==board[8]!=0 or board[0]==board[3]==board[6]!=0 or board[7]==board[4]==board[1]!=0 or board[2]==board[5]==board[8]!=0 or board[0]==board[4]==board[8]!=0 or board[2]==board[4]==board[6]!=0:
        print("")           
        print("**************")
        print("Game won by Player " + str(player))
        print("🎉")
        print("**************")
        return 1
    elif slotFilled==9:
        print("")           
        print("**************")
        print("Game Tied")
        print("     😑")
        print("**************")
        return 1
    return 0
             
#Game sequence
drawBoard()
while 1:
    _input = input("It's your turn Player "+str(player)+" :  ")
    if _input.strip().isdigit() and int(_input.strip()) >= 1 and int(_input.strip()) <= 9:
        if board[int(_input.strip()) - 1] != 0:
            print("That place is already occupied, Sorry")
        else:
            board[int(_input.strip()) - 1] = player
            drawBoard()
            if player == X:
                player = O
            else:
                player = X
            slotFilled = slotFilled + 1
    else:
        print("Looks like you have made a typing mistake")
        print("Try Again!!")
    if checkGameResult():
        while 1:
            x = input("Would you like to play again?? Y/N :  ")
            if x == "y":
                player = X
                break
            elif x == "n":
                sys.exit("Player did not want to play again")
            else:
                print("Sorry, We didn't understand")
        
 
