import unittest
from scenario import Scenario

class ScenarioInitTests(unittest.TestCase):

    def test_that_scenario_has_tokens(self):
        scenario = Scenario("x","o")
        self.assertEqual("x",scenario.player_one_token)
	self.assertEqual("o",scenario.player_two_token)
	
    def test_that_scenario_has_setup(self):
	scenario = Scenario("x","o")
	scenario_attributes_and_methods = dir(scenario)
        self.assertTrue("setup" in scenario_attributes_and_methods)
	
