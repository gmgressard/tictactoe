board = ['_1_', '_2_', '_3_','_4_', '_5_', '_6_','_7_', '_8_', '_9_']


def print_board():
    """print game board"""

    print(board[0] + '|' + board[1] + '|' + board[2])
    print(board[3] + '|' + board[4] + '|' + board[5])
    print(board[6] + '|' + board[7] + '|' + board[8])


def play_game():
    """game logic"""

    print_board()
    count = 0 
    
    while count <= 9:
        if check_winner() == False and count == 9:
            print('*' * 20)
            print("It's a Tie")
            print('*' * 20)
            break
        elif check_winner() == False and count < 9 and count %2 == 0 :
            play_turn('_X_')
            print_board()
            check_winner()
            count+=1
            if check_winner() == True:
                print('*' * 20)
                print('X is the is winner!')
                print('*' * 20)
                break 
        elif check_winner() == False and count < 9 and count %2 != 0:
            play_turn('_O_')
            print_board()
            check_winner()
            count+=1
            if check_winner() == True:
                print('*' * 20)
                print('O is the winner!')
                print('*' * 20)
                break 
  

def play_turn(player):
    """update spot on board with user input"""

    user_input = input('Where would like to play (choose empty spot 1 - 9) ? > ')        
    user_input_i = int(user_input) - 1
    board[user_input_i] = player
   

def check_winner():
    """check for winner on board"""

    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for win in wins:
        for player in ['_X_', '_O_']:
            if board[win[0]] == board[win[1]] == board[win[2]] == player:
                return True 
    return False 

                

play_game()