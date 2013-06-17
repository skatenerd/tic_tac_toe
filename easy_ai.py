from ai import AI
import random

class EasyAI(AI):

    def next_move(self,board):
        move_list = self.__build_move_list__(board)
        easy_move_list = filter(lambda x: x[0] < 1, move_list)
        move = random.choice(easy_move_list)
        return move