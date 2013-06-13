class PlayerInput(object):

    def call(self):
        return raw_input()

class InputValidator(object):

    def validate(self,player,valid_responses,data_type=int):
        response = None
        while response not in valid_responses:
            try:
                response = data_type(player.next_move())
            except:
                continue
        return response
