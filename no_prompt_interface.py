from game import Game

class NoPromptInterface(object):


    def setup(self,player_object):
	return Game(player_object("x"),player_object("o"))

    @staticmethod
    def flags():
        return {"token_flag":False,
	        "difficulty_flag":False,
		"order_flag":False}
