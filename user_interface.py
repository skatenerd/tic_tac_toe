from __future__ import print_function
from collections import OrderedDict
from game import Game
from playerinput import InputValidator
from printer import Printer
from scenario_selector import ScenarioSelector

class UserInterface(object):

    def __init__(self,user_input,display_object=Printer()):
        self.user_input = user_input
        self.display_method = display_object.display
       
    def game_setup(self):
	scenario_number = self.pick_scenario()
	scenario_selector = ScenarioSelector(scenario_number)
	flags = scenario_selector.scenario_flags()
	user_responses = self.show_flagged_prompts_and_get_input(flags) 
	token = user_responses.get("token")
	opposite_token = {"o":"x","x":"o",None:""}[token] 
	difficulty = user_responses.get("difficulty")
	order = user_responses.get("order")
	scenario = scenario_selector.return_scenario(token,opposite_token,
			                             order,difficulty)
        return scenario.setup() 

    def show_flagged_prompts_and_get_input(self,flags):
	prompts = OrderedDict()
        prompts[self.pick_order] = flags["order_flag"]
	prompts[self.pick_token] = flags["token_flag"]
	prompts[self.pick_difficulty] = flags["difficulty_flag"]
	answer_list = {} 
        for prompt in prompts:
	    flag = prompts[prompt]
	    if flag: 
		answer = prompt()
	        answer_list.update(answer)
	return answer_list

    def pick_order(self):
        prompt = "Would you like to move first or second (1,2): "
        player_response = self.__prompt_loop__(prompt, (1,2))
	return {"order":player_response}

    def pick_token(self):
        prompt = "Would you like to play as x or o: "
        token = self.__prompt_loop__(prompt, ("x","o"))
	return {"token": token}

    def pick_difficulty(self):
        prompt = "Would like to play against an easy or impossible ai: "
        difficulty = self.__prompt_loop__(prompt,("easy","impossible"))
	return {"difficulty":difficulty}
    
    def pick_scenario(self):
        prompt = ("Please choose a scenario: \n" +
                  "(1) Human vs AI\n" +
                  "(2) Human vs Human\n" +
                  "(3) AI vs AI\n"
                  "(4) Humanoid vs AI")
        scenario = self.__prompt_loop__(prompt,(1,2,3,4))
        return scenario
 
    def __prompt_loop__(self,prompt,valid_responses):
        self.display_method(prompt)
        validator = InputValidator()
        response = validator.return_valid_response(self.user_input, (valid_responses))
        return response
