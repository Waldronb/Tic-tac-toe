

def main():

    player1 = input("Please pick a marker 'X' or 'O' ")
    toe_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    win = False

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    turn = 0
    board(toe_board)
    while win == False:

        toe_board = players_turn(toe_board, player1, player2, turn)
        print('\n'*10)
        board(toe_board)
        win = check(toe_board)

        turn += 1
        if turn > 8:
            break

    if win and turn % 2 == 0:
        print('Player 2 Wins!!!')
    elif win and turn % 2 == 1:
        print('Player 1 Wins!@!!')
    else:
        print("Cat's game, please play again: ")


def check(toe_board):
    win = False
    if toe_board[0] == toe_board[1] and toe_board[1] == toe_board[2]:
        win = True
    if toe_board[0] == toe_board[3] and toe_board[3] == toe_board[6]:
        win = True
    if toe_board[0] == toe_board[4] and toe_board[4] == toe_board[8]:
        win = True
    if toe_board[1] == toe_board[4] and toe_board[4] == toe_board[7]:
        win = True
    if toe_board[6] == toe_board[4] and toe_board[4] == toe_board[2]:
        win = True
    if toe_board[2] == toe_board[5] and toe_board[5] == toe_board[8]:
        win = True
    if toe_board[3] == toe_board[4] and toe_board[4] == toe_board[5]:
        win = True
    if toe_board[6] == toe_board[7] and toe_board[7] == toe_board[8]:
        win = True
    return win


def board(toe_board):

    print(' ' + str(toe_board[0]) + ' ' + '|' + ' ' + toe_board[1] + ' ' + '|' + ' ' + toe_board[2])
    print('----------')
    print(' ' + toe_board[3] + ' ' + '|' + ' ' + toe_board[4] + ' ' + '|' + ' ' + toe_board[5])
    print('----------')
    print(' ' + toe_board[6] + ' ' + '|' + ' ' + toe_board[7] + ' ' + '|' + ' ' + toe_board[8])


def players_turn(toe_board, player1, player2, turn):
    print('\n')

    if turn % 2 == 0:

        position = input('Player 1 where would you like to go?\n\n\n ')
        mark = player1
    else:
        position = input("Player 2 where would you like to go?\n\n\n ")
        mark = player2
    for i in range(len(toe_board)):
        if position == toe_board[i]:
            toe_board[i] = mark
    return toe_board


main()