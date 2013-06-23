from test_utils import MockUserInput, MockPlayer
import unittest
from playerinput import InputValidator

class InputValidatorTests(unittest.TestCase):

  def test_that_it_returns_a_str(self):
      valid_response = ("a","b")
      input_source = MockUserInput([7,"c","a"])
      validator = InputValidator()
      self.assertEqual("a",validator.return_valid_response(input_source,valid_response))

  def test_that_it_can_convert_types(self):
      valid_responses = ("2")
      input_source = MockUserInput([7,"c","a",2])
      validator = InputValidator()
      self.assertEqual("2",validator.return_valid_response(input_source,valid_responses))

  def test_that_it_can_return_int(self):
      valid_responses = (1,2,3)
      input_source = MockUserInput(["a","b",7,2])
      validator = InputValidator()
      self.assertEqual(2,validator.return_valid_response(input_source,valid_responses))
 
