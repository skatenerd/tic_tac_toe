from ai import AI
import random

class EasyAI(AI):

    def next_move(self,board):
        move_list = self.__build_move_list__(board)
        easy_move_list = filter(self.lowest_scores,move_list)
        if easy_move_list:
            move = random.choice(easy_move_list)[1]
        else:
            move = random.choice(move_list)[1]
        return move

    def lowest_scores(self,move_list):
        score = move_list[0] 
	return score <= 0	
