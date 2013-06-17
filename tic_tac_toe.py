from user_interface import UserInterface
from playerinput import PlayerInput

if __name__ == "__main__":
    ui = UserInterface(user_input=PlayerInput())
    game = ui.game_setup()
    game.run()
