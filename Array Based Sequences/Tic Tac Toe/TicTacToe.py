class TicTacToe:
    """Management of a Tic Tac Toe game(Does not do strategy)"""

    def __init__(self):
        """Start a new game"""
        self._board = [[''] * 3 for j in range(3)]
        self._player_mark = 'X'

    def mark(self, i, j):
        """Make new mark in the game"""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Index out of bounds")
        if self._board[i][j] != '':
            raise ValueError('Current position already filled')
        if self.winner() is not None:
            raise ValueError('Game already complete!!')
        self._board[i][j] = self._player_mark

        if self._player_mark == 'X':
            self._player_mark = 'O'
        else:
            self._player_mark = 'X'

    def _is_win(self, mark):
        """Check whether the board configuration is win for the given player"""
        board = self._board                                           # Local Variable for shorthand
        return (self._rows_complete(mark, board) or self._columns_complete(mark, board) or
                self._diagonals_complete(mark, board))

    def _rows_complete(self, mark, board):
        return (mark == board[0][0] == board[0][1] == board[0][2]     # row 0
                or mark == board[1][0] == board[1][1] == board[1][2]  # row 1
                or mark == board[2][0] == board[2][1] == board[2][2]  # row 2
                )

    def _columns_complete(self, mark, board):
        return (mark == board[0][0] == board[1][0] == board[2][0]     # column 0
                or mark == board[0][1] == board[1][1] == board[2][1]  # column 1
                or mark == board[0][2] == board[1][2] == board[2][2]  # column 2
                )

    def _diagonals_complete(self, mark, board):
        return (mark == board[0][0] == board[1][1] == board[2][2]     # diagonal
                or mark == board[0][2] == board[1][1] == board[2][0]  # reverse diagonal
                )

    def winner(self):
        """Return mark of winning player or None to indicate a tie"""

        for i in 'XO':
            if self._is_win(i):
                return i
        return None

    def __str__(self):
        """Return string representation of the current board"""
        rows = ['|'.join(self._board[r]) for r in range(3)]
        return '\n---\n'.join(rows)
