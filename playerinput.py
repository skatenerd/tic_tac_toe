class PlayerInput(object):

    def call(self):
        return raw_input()

class MoveValidator(object):

    def validate(self,board,player,valid_responses,data_type=int):
        response = None
	while response not in valid_responses:
	    try:
	        response = data_type(player.next_move(board))
	    except:
		continue
	return response

class InputValidator(object):

    @staticmethod
    def return_valid_response(input_source,valid_responses):
        data_type = type(valid_responses[0])
        user_input = " "
        while user_input not in valid_responses:
            try:
                user_input = data_type(input_source.call())
            except:
                continue
        return user_input
