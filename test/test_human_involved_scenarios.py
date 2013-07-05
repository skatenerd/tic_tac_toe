import unittest
from human_prompt_interface import HumanPromptInterface
from game import Game
from ai import ImpossibleAI
from easy_ai import EasyAI
from player import HumanPlayer
from human_vs_ai import HumanVsAiScenario

class SetupTests(unittest.TestCase):

    def test_setup_observes_user_data(self):
      game = HumanVsAiScenario.game({
        HumanPromptInterface.order_prompt() : "2",
        HumanPromptInterface.token_prompt() : "x",
        HumanPromptInterface.difficulty_prompt() : "easy",
      })
      self.assertTrue(isinstance(game.player_two, HumanPlayer))
      self.assertTrue(isinstance(game.player_one, EasyAI))
      self.assertEqual(game.player_one.token, "o")
      self.assertEqual(game.player_two.token, "x")
