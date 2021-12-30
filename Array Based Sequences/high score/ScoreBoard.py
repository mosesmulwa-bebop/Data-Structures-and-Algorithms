class ScoreBoard:
    """Score board of all high scores in the game.
    Index 0 - the highest score
    Capacity - Number of high scores we want to store
    """

    def __init__(self, capacity=10):
        self._board = [None] * capacity  # Create an empty list called Board of length capacity
        self._n = 0                      # Number of actual entries

    def __getitem__(self, k):
        """Return entry at index k"""
        return self._board[k]

    def __str__(self):
        """Return a string representation of the high score list"""
        return '\n'.join(str(self._board[j]) for j in range(self._n))

    def add(self, entry):
        """Add a new entry to the list"""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # Answer is yes if board not full or score is higher than last entry
        # The last entry is the lowest

        good = self._n < len(self._board) or score > self._board[-1].get_score()

        if good:
            if self._n < len(self._board):                  # no score drops from list
                self._n += 1                                # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self._n - 1
            while j > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]           # shift entry from j-1 to j
                j -= 1
            self._board[j] = entry


