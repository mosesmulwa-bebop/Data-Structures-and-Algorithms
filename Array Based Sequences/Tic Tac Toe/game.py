from TicTacToe import TicTacToe

game = TicTacToe()
# X moves:          # O moves:
game.mark(1, 1);    game.mark(0, 2)
game.mark(2, 2);    game.mark(0, 0)
game.mark(0, 1);    game.mark(2, 1)
game.mark(1, 2);    game.mark(1, 0)
game.mark(2, 0)

print(game)
winner = game.winner()

if winner is None:
    print('Tie')
else:
    print(winner, 'wins')
