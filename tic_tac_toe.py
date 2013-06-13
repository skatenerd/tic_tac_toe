from game import Game
from player import Player
from ai import AI

if __name__ == "__main__":
    game = Game(Player("x"),AI("o"))
    game.run()




