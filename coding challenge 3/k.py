board=[' _ 'for X in range(9)]
player =" X "


win_combination= [[0,1,2] ,[3,4,5] ,[6,7,8],
                  [0,3,6] ,[1,4,7] ,[2,5,8],
                  [0,4,8] ,[2,4,6]]         

def draw_board():
    print ('  -----------------')
    print (' | '+board[0]+' | '+board[1]+' | '+board[2]+' | ')
    print ('  -----------------')
    print (' | '+board[3]+' | '+board[4]+' | '+board[5]+' | ')
    print ('  -----------------')
    print (' | '+board[6]+' | '+board[7]+' | '+board[8]+' | ')
    print ('  -----------------')
def play_turn():
    move = input("Where do you want to make a move (1-9) :")
    move = int(move) - 1

    board[move] =player
 
def change_player():
    global player
    if player == " X ":
        player =" O "
    else:
        if player ==" O ":
            player =" X "


def check_win():
    for i,h,r in win_combination:
        if board[i] ==board[h] == board[r] !=' - ':
            print(player +'wins!')

        else:
            continue

def play_the_game():
    while True:
        draw_board()
        play_turn()
        check_win()
        change_player()



play_the_game()