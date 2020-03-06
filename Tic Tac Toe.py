# TIC TAC TOE

import random

# Function to display the tic tac toe board
def display_board(board):
    print('  |   |')
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('  |   |')
    print('---------------')
    print('  |   |')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('  |   |')
    print('--------------')
    print('  |   |')
    print(board[1]+' | '+board[2]+' | '+board[3])
    print('  |   |')

# Function to allow player 1 to choose his sign and gives player 2 the other sign
def player_input():
    sign =''
    while sign!='X' and sign!='O':
        sign = input('Player1 Please enter X or O').upper()
    if sign=='X':
        return ('X','O')
    else:
        return ('O','X')

# Function to place the sign in entered position
def place(board,sign,position):
    board[position] = sign

# Function to define all the winning conditions
def win(board,sign):
    return((board[1] == sign and board[2]  == sign and  board[3] == sign) or
    (board[4] == sign and board[5]  == sign and  board[6] == sign) or
    (board[7] == sign and board[8]  == sign and  board[9] == sign) or
    (board[1] == sign and board[4]  == sign and  board[7] == sign) or
    (board[2] == sign and board[5]  == sign and  board[8] == sign) or
    (board[3] == sign and board[6]  == sign and  board[9] == sign) or
    (board[1] == sign and board[5]  == sign and  board[9] == sign) or
    (board[3] == sign and board[5]  == sign and  board[7] == sign))

# Function to randomly select which player will start with the Game
def start():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

# Function to check if there is any space left on the board
def space_check(board,position):
    return (board[position] == ' ')

# Function to check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Function to take the positions from users
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position

# Function to allow users to replay the Game
def replay():
    choice= input("PLAY AGAIN? Enter Yes or No").upper()
    return choice == 'YES'


# Game logic
print("Welcome to Tic Tac Toe.!")
while True:
    board = [' ']*10
    player1_sign , player2_sign = player_input()
    turn = start()
    print(turn + ' will go first')
    play_game = input('Ready to play? Y or N').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        # For Player 1
        if turn == 'Player 1':
            display_board(board)
            print('Player 1:')
            position = player_choice(board)
            place(board,player1_sign,position)

            if win(board,player1_sign):
                display_board(board)
                print('PLAYER 1 HAS WON')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    game_on = False 
                else:
                    turn = 'Player 2'                    
        else:
            # For Player 2
            display_board(board)
            print('Player 2:')
            position = player_choice(board)
            place(board,player2_sign,position)
 
            if win(board,player2_sign):
                display_board(board)
                print('PLAYER 2 HAS WON!!')
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME!")
                    game_on = False 
                else:
                    turn = 'Player 1'
    
    if not replay():
        break
