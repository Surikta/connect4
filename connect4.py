import numpy as np


def vertical_win(board):

    win = 0
    for i in range(len(board[0, :])):
        for j in range(4):
            if ([1, 1, 1, 1] == board[j:j+4, i]).all():
                win = 1
                break
            elif ([2, 2, 2, 2] == board[j:j+4, i]).all():
                win = 1
                break

        if win == 1:
            break

    return win


def horizontal_win(board):

    win = 0
    if win == 0:
        for i in range(len(board[:, 0])):
            for j in range(4):
                if ([1, 1, 1, 1] == board[i, j:j + 4]).all():
                    win = 1
                    break
                elif ([2, 2, 2, 2] == board[i, j:j + 4]).all():
                    win = 1
                    break

            if win == 1:
                break

    return win


def diagonal_win(board):

    win = 0

    # Checks 3 cases:
    # - From columns 1,2 and 3 the only way to win is in the right direction ↘
    # - From columns 5,6 and 7 the only way to win is in the left direction ↙
    # - From column 4 both cases are possible
    for i in range(4):
        for j in range(7):
            diag_arr = []
            # Case 1
            if j < 3:
                for k in range(4):
                    diag_arr = np.append(diag_arr, board[i+k, j+k])

                if ([1, 1, 1, 1] == diag_arr).all():
                    win = 1
                    break

                if ([2, 2, 2, 2] == diag_arr).all():
                    win = 1
                    break

            # Case 2
            if j > 3:
                for k in range(4):
                    diag_arr = np.append(diag_arr, board[i+k, j-k])

                if ([1, 1, 1, 1] == diag_arr).all():
                    win = 1
                    break

                if ([2, 2, 2, 2] == diag_arr).all():
                    win = 1
                    break

            # Case 3
            if j == 3:
                for k in range(4):
                    diag_arr = np.append(diag_arr, board[i+k, j-k])

                if ([1, 1, 1, 1] == diag_arr).all():
                    win = 1
                    break

                if ([2, 2, 2, 2] == diag_arr).all():
                    win = 1
                    break

                if win == 1:
                    break
                else:
                    diag_arr = []
                    for k in range(4):
                        diag_arr = np.append(diag_arr, board[i + k, j + k])

                    if ([1, 1, 1, 1] == diag_arr).all():
                        win = 1
                        break

                    if ([2, 2, 2, 2] == diag_arr).all():
                        win = 1
                        break

        if win == 1:
            break

    return win


def winner(game_table):
    v_win = vertical_win(board=game_table)
    h_win = horizontal_win(board=game_table)
    d_win = diagonal_win(board=game_table)
    win = np.max([v_win, h_win, d_win])

    return win


def player_change(game_player):
    if game_player == "Player 1":
        game_player = "Player 2"
    else:
        game_player = "Player 1"

    return game_player

