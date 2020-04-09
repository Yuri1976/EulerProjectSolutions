from IPython.display import clear_output

import random

def display_board(board):
    clear_output()
    print('   |   |')
    print (' '+ board[7] +' | '+board[8]+' | '+board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+ board[4] +' | '+board[5]+' | '+board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print (' '+ board[1] +' | '+board[2]+' | '+board[3])
    print('   |   |')

def player_input():
    '''
    OUTPUT IS A TUPLE (Player1, Player2)
    '''
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker=input('Player1: Choose X or O: ').upper()
        
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def choose_first():
    flip = random.randint(0,1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    if " " in board[1:]:
        return False
    else:
        return True

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
    
    return position

def replay():
    
    choice = input('Play again? Enter Yes or No: ')
    
    return choice == 'Yes'

#WHILE LOOP TO PLAY THE GAME
print('Welcome to tic tac toe')

while True:
    #PLAY THE GAME
    
    ##SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board =[' ']*10
    player1_marker,player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Ready to play? y or n?')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    ##GAME PLAY
    while game_on:
        ##PLAY ONE TURN
        if turn == 'Player 1':
            #SHOW THE BOARD
            display_board(the_board)
            #CHOOSE A POSITION
            position = player_choice(the_board)
            #PLACE THE MARKER
            place_marker(the_board,player1_marker, position)
            
            #IF THEY WON
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 won!')
                game_on = False
                
            #IF THERE IS A TIE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('is a tie')
                    game_on = False
                
                else:
                    turn = 'Player 2'
            
          
        ##PLAY TWO TURN
        else:
            #SHOW THE BOARD
            display_board(the_board)
            #CHOOSE A POSITION
            position = player_choice(the_board)
            #PLACE THE MARKER
            place_marker(the_board,player2_marker, position)
            
            #IF THEY WON
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 won!')
                game_on = False
                
            #IF THERE IS A TIE
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('is a tie')
                    game_on = False

                else:
                    turn = 'Player 1'
    
    if not replay():
        break
    #BREAK OUT OF THE WHILE LOOP ON REPLAY()