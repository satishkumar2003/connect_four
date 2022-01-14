import numpy as np

#printing the board neatly
def print_board(_board):
    for i in _board:
        for j in i:
            print(int(j),end=' ')
        print()

#function that inserts the number as per the player number and available spaces
def insert_1(_board,coloumn,player):
    for i in range(5,-1,-1):
        if _board[i][coloumn]==0:
            _board[i][coloumn]=player
            break
    return _board

#Winning situation

def check_for_win(_board,player_no):
    #vertical line win
    for i in range(len(_board)-3):
        for j in range(len(_board[i])):
            if _board[i][j]==player_no and _board[i+1][j]==player_no and _board[i+2][j]==player_no and _board[i+3][j]==player_no:
                return True
            
    #horizontal line win
    for i in range(len(_board)):
        for j in range(len(_board[i])-3):
            if _board[i][j]==player_no and _board[i][j+1]==player_no and _board[i][j+2]==player_no and _board[i][j+3]==player_no:
                return True

    #45degree line win
    for i in range(len(_board)-3):
        for j in range(len(_board[i])-3):
            if _board[i][j]==player_no and _board[i+1][j+1]==player_no and _board[i+2][j+2]==player_no and _board[i+3][j+3]==player_no:
                return True            
    
    #-45degree line win
    for i in range(len(_board)-3):
        for j in range(3,len(_board[i])):
            if _board[i][j]==player_no and _board[i-1][j+1]==player_no and _board[i-2][j+2]==player_no and _board[i-3][j+3]==player_no:
                return True
    


#Initialising the board
board = np.zeros((6,7))

#Game starts

game_end = False
turn = 1

print_board(board)
while not game_end:
    turn_decide = turn%2
    if turn_decide==1:
        coords = int(input("Player 1 enter the colomn number (0,6): "))
        board = insert_1(board,coords,1)
        if check_for_win(board,1):
            print("Player 1 wins!!!")
            game_end=True
    else:
        coords = int(input("Player 2 enter the colomn number (0,6): "))
        board = insert_1(board,coords,2)
        if check_for_win(board,2):
            print("Player 2 wins!!!")
            game_end=True        
    print_board(board)
    if turn>42:
        game_end=True
        print("It's a draw!!")
    turn +=1
