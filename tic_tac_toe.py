import os
from time import sleep

turn = 1
board = {
         '1': '.', '2': '.', '3': '.',
         '4': '.', '5': '.', '6': '.',
         '7': '.', '8': '.', '9': '.'
         }


def print_board():
    _ = os.system('cls')
    print('\n\t|', board['1'], '|', board['2'], '|', board['3'], '|',
          '\n\t|', board['4'], '|', board['5'], '|', board['6'], '|',
          '\n\t|', board['7'], '|', board['8'], '|', board['9'], '|')


def move():
    global turn
    if turn % 2 == 1:
        player = 'X'
    else:
        player = 'O'
    print('\nPlayer:', player)
    choice = input('Choose a position from 1 to 9: ')
    try:
        if 0 < int(choice) < 10 and board[choice] == '.':
            board[choice] = player
            turn += 1
        else:
            print('\nUnfortunate selection\nTry again\n')
            sleep(2)
    except ValueError:
        print('\nPlease, type only numbers between 1 and 9')
        sleep(2)


def winner():
    for r in (1, 2, 3, 4, 7):
        # Check diagonals:
        if r == 1 and ((board[str(r)] == board[str(r+4)] == board[str(r+8)]
                        != '.') or
                       (board[str(r+2)] == board[str(r+4)] == board[str(r+6)]
                        != '.')):
            return (True, board[str(r+4)])
        # Check columns:
        if r < 4 and (board[str(r)] == board[str(r+3)] == board[str(r+6)]
                      != '.'):
            return (True, board[str(r)])
        # Check rows:
        if ((not 1 < r < 4) and
           (board[str(r)] == board[str(r+1)] == board[str(r+2)] != '.')):
            return [True, board[str(r)]]
    return (False, '')


def run_game():
    global turn
    print_board()
    while turn < 10:
        move()
        check_winner = winner()
        print_board()
        if check_winner[0]:
            print('\nThe winner is:', check_winner[1])
            exit()
    print('\n\n\tTIE\n')


run_game()
