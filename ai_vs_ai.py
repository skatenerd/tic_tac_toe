from ai import AI
from game import Game
from scenario import Scenario

class AiVsAiScenario(Scenario):

    def setup(self):
        player_one = AI(self.player_one_token)
	player_two = AI(self.player_two_token)
	return Game(player_one,player_two)
