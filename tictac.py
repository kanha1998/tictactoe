   
def display_board(board):
    #clear_output
    print('   |  |  ')
    print('  '+board[7]+'| '+board[8]+'|'+board[9])
    print('   |  |  ')
    print('-----------')
    print('   |  |  ')
    print('  '+board[4]+'| '+board[5]+'|'+board[6])
    print('   |  |  ')
    print('-----------')
    print('   |  |  ')
    print('  '+board[3]+'| '+board[2]+'|'+board[1])
    print('   |  |  ')
    
    
 
def player_input():
    marker =''
    while not (marker=='X' or marker =='O' ):
        marker = input('enter choise X or O for player 1').upper()
        
    if (marker == 'X'):
         return('X','O')
    else:
         return('O','X')

def place_marker(board,postion,marker):
    board[postion]=marker;
def check_win(board,marker):
    return ((board[7]==marker and board[8]== marker and board[9]== marker) or
            (board[4]==marker and board[5]== marker and board[6]== marker) or
            (board[3]==marker and board[2]== marker and board[1]== marker) or
            (board[7]==marker and board[4]== marker and board[3]== marker) or
            (board[8]==marker and board[5]== marker and board[2]== marker) or
            (board[9]==marker and board[6]== marker and board[1]== marker) or
            (board[7]==marker and board[5]== marker and board[1]== marker) or
            (board[3]==marker and board[5]== marker and board[9]== marker))
import random
def choose_first():
    if (random.randint(0,1)== 0):
        return 'player 2';
    else:
        return 'player 1';
def space_check(board,postion):
    
    return (board[postion]==' ')
def full_board_check(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    else:
        return  True       
def player_choice(board):
    postion=' '
    while postion not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(postion)):
        postion = input('enter next  postion (1,9)')
    return int(postion)    
def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print("welcome to tic tac toe")

while True:
    theboard=[' ']*10
    player1_marker,player2_marker=player_input();
    turn=choose_first()
    print(turn+'first turn first')
    game_on=True
    
    while game_on:
        if turn == 'player 1':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,position,player1_marker)
            
            if check_win(theboard,player1_marker):
                display(theboard)
                print("congratulation player1 won")
                game_on = False
            else:
                if full_board_check(theboard):
                    display(theboard)
                    print('game draw')
                    break;
                else:
                    turn ='player 2'
        if turn == 'player 2':
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard,position,player2_marker)
            
            if check_win(theboard,player2_marker):
                display(theboard)
                print("congratulation player2 won")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print('game draw')
                    break;
                else:
                    turn ='player 1' 
    if not replay():
            break;
                                            
        