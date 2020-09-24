''' Tic Tac Toe for 2 players in Python '''
# Made by :Pratham Prasoon, Yaksh Bariya
# Twitter @PrassonPratham , @CodingThunder
   
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
    print("| " + boxValue(1) + " | " + boxValue(2) + ' | '+ boxValue(1) + ' |')
    print("|-----------|" )
    print("| " + boxValue(4) + " | " + boxValue(5) + ' | '+ boxValue(1) + ' |' )
    print("|-----------|"  )
    print("| " + boxValue(7) + " | " + boxValue(8) + ' | '+ boxValue(1) + ' |')
    print("-------------" ) 
    print("It's your turn Player "+player+" :  ")
 
#Check if the game has been won or Tied 
def checkGameWon():
    if board[0]==board[1]==board[2] or board[3]==board[4]==board[5] or board[6]==board[7]==board[8] or board[0]==board[3]==board[6] or board[7]==board[4]==board[1] or board[2]==board[5]==board[8] or board[0]==board[4]==board[8] or board[2]==board[4]==board[6]:
        print("")           
        print("**************")
        print("Game won by " + player)
        print("🎉")
        print("**************")
    elif slotFilled==9:
        print("")           
        print("**************")
        print("Game Tied")
        print("     😑")
        print("**************")
             
#Game sequence
#Write code here👇     
        
 
