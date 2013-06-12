class PlayerInput(object):

    def output(self):
        return raw_input()

class InputValidator(object):

    def __init__(self,input_source):
        self.input_source = input_source

    def validate(self,valid_responses,data_type=int):
        user_input = None
        while user_input not in valid_responses:
            try:
                user_input = data_type(self.input_source.output())
            except:
                continue
        return user_input