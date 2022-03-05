import numpy as np
from connect4 import *


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
