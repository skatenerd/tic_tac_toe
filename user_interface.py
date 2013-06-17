from __future__ import print_function
from game import Game
from player import Player
from ai import AI
from easy_ai import EasyAI
from playerinput import InputValidator

class UserInterface(object):

    def __init__(self,user_input,display_object="python_print"):
        self.user_input = user_input
        self.display_method = display_object.print_this if not display_object == "python_print" else print
        
    def game_setup(self):
        order = self.pick_order()
        token = self.pick_token()
        opposite_token = {"o":"x","x":"o"}[token]
        difficulty = self.pick_difficulty()
        ai = {"easy":EasyAI,"impossible":AI}[difficulty]
        order_hash = {1:(Player(token),ai(opposite_token)),2:(ai(opposite_token),Player(token))}
        player_one, player_two = order_hash[order]
        return Game(player_one,player_two)

    def pick_order(self):
        prompt = "Would you like to move first or second (1,2): "
        player_response = self.__prompt_loop__(prompt, (1,2))
        return player_response

    def pick_token(self):
        prompt = "Would you like to play as x or o: "
        token = self.__prompt_loop__(prompt, ("x","o"))
        return token

    def pick_difficulty(self):
        prompt = "Would like to play against an easy or impossible ai: "
        difficulty = self.__prompt_loop__(prompt,("easy","impossible"))
        return difficulty

    def __prompt_loop__(self,prompt,valid_responses):
        self.display_method(prompt)
        validator = InputValidator()
        response = validator.return_valid_response(self.user_input, (valid_responses))
        return response