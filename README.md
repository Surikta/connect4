# connect4
Simple connect 4 game using numpy in python


The idea starts by creating a 7x7 0 matrix.

```python
import numpy as np

print(str(np.zeros(shape=(7, 7))))
[[0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0.]]
```

Each element in the matrix represents a space in the connect 4 game board.
We start by importing the connect4.py file and create a Table class.


```python
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
```

The Table class creates the board ready to play. The initial states creates the empty board and 'Player 1' moves first.
To play we set the position we want to fill from 1 to 7. The player 1 uses the ⊗ symbol and the player 2 uses the ⊙ symbol (those can be changed).

```python
table = Table()
table.play(4)
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 ⊗ 〇 〇 〇
 table.play(3)
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 ⊙ ⊗ 〇 〇 〇
  table.play(4)
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 ⊗ 〇 〇 〇
 〇 〇 ⊙ ⊗ 〇 〇 〇
```

After a some turns the game is over and ressets the the initial state.

```python
table.play(5)
table.play(4)
table.play(2)
table.play(4)
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 〇 〇 〇 〇
 〇 〇 〇 ⊗ 〇 〇 〇
 〇 〇 〇 ⊗ 〇 〇 〇
 〇 〇 〇 ⊗ 〇 〇 〇
 〇 ⊙ ⊙ ⊗ ⊙ 〇 〇
 
Winner is Player 1
```
This simple game can be used to train an AI to play connect 4, the state can be accessed by

```python
table.table
array([[0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 1., 2., 0., 0., 0.]])
```

Returns a matrix with elements 0, 1 and 2 (1 and 2 represents the player)
