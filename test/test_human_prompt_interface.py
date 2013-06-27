import unittest
from human_prompt_interface import HumanPromptInterface

class HumanPromptInterfaceFlagsTests(unittest.TestCase):

    def test_that_it_returns_appropriate_flags(self):
	flags = HumanPromptInterface.prompt_flags()
	self.assertTrue("token_flag" in flags)
	self.assertTrue("difficulty_flag" in flags)
	self.assertTrue("order_flag" in flags)

