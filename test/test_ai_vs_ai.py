import unittest
from ai import ImpossibleAI
from easy_ai import EasyAI
from ai_vs_ai import AiVsAiScenario

class AiVsAiScenarioTests(unittest.TestCase):

    def test_listens_to_easy_difficulty(self):
      user_data = {
          "What difficulty would you like the first ai to be (easy,impossible): ":
          "impossible"
      }
      game = AiVsAiScenario(user_data).game()
      self.assertIsInstance(game.player_one, ImpossibleAI)

    def test_listens_to_easy_difficulty(self):
      user_data = {
          "What difficulty would you like the first ai to be (easy,impossible): ":
          "easy"
      }
      game = AiVsAiScenario(user_data).game()
      self.assertIsInstance(game.player_one, EasyAI)

