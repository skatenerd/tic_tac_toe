import game
from player import Player
from ai import AI
from board import Board
from playerinput import PlayerInput

if __name__ == "__main__":

    token = raw_input("Would you like to be x or o: ")
    order = int(raw_input("Would you like to go first or second(1,2): "))
    human_player = Player(token)
    computer = AI(human_player.opponent_token)
    if order == 1:
        game = game.Game(human_player,computer)
    else:
        game = game.Game(computer,human_player)
    game.run()

    if game.gameboard.winner():
        print game.gameboard.winner() + " wins!"
    else:
        print "It's a tie!"

