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


class Table:
    # Initial state of the board (starts player 1)
    def __init__(self):
        self.table = np.zeros(shape=(7, 7))
        self.player = "Player 1"

    # Resets the game
    def reset(self):
        self.table = np.zeros(shape=(7, 7))
        self.player = "Player 1"

    def play(self, position):

        # Calculates the vertical position of the coin
        v_position = 6
        for i in range(7):
            # If it finds a coin there, returns the position above
            if self.table[i, position - 1] != 0:
                v_position = i - 1
                break

        self.table[v_position, position - 1] = int(self.player[len(self.player)-1])

        # Shows the state of the board
        board = str(self.table).replace("1", chr(8855)).replace("2", chr(8857)).replace(".", "")
        board = board.replace("0", chr(12295)).replace("[[", " ").replace("[", "").replace("]", "")
        print(board)
        print("\n")

        # Checks if the game is over
        win = winner(game_table=self.table)
        if win == 1:
            print('Winner is ' + self.player)
            self.reset()
        else:
            self.player = player_change(self.player)


table = Table()
