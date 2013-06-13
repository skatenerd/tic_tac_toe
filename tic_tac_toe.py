from __future__ import print_function
from game import Game
from player import Player
from ai import AI
from playerinput import InputValidator

if __name__ == "__main__":
    game = game_setup()
    game.run()


def game_setup(user_input,display_object="python_print"):
    display_method = display_object.print_this if not display_object == "python_print" else print
    display_method("Would you like to move first or second: ")
    player_response = None
    while player_response not in (1,2):
        player_response = user_input.call()
    order_hash = {1:(Player("x"),AI("o")),2:(AI("o"),Player("x"))}
    player_one, player_two = order_hash[player_response]
    display_method("Would you like to play as x or o: ")
    return Game(player_one,player_two)



