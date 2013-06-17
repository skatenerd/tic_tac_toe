from __future__ import print_function
from game import Game
from player import Player
from ai import AI
from playerinput import PlayerInput, InputValidator

if __name__ == "__main__":
    game = Game(Player("x"),AI("o"))
    game.run()

def game_setup(user_input,display_object="python_print"):
    display_method = display_object.print_this if not display_object == "python_print" else print
    player_response = pick_order(user_input,display_method)
    display_method("Would you like to play as x or o: ")
    order_hash = {1:(Player("x"),AI("o")),2:(AI("o"),Player("x"))}
    player_one, player_two = order_hash[player_response]
    return Game(player_one,player_two)

def pick_order(user_input,display_method):
    display_method("Would you like to move first or second: ")
    player_response = None
    while player_response not in (1,2):
        player_response = int(user_input.call())
    return player_response

def pick_token(user_input,display_method):
    display_method("Would you like to play as x or o: ")
    token = None
    while token not in ("x","o"):
        token = str(user_input.call())
    return token