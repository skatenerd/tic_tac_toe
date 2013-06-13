#file is misnamed?
#also, did it feel natural to test-drive this class?
import sys
sys.path.append("../")
from test_utils import MockUserInput
from board import Board
import unittest
from playerinput import InputValidator

class InputValidatorTests(unittest.TestCase):

  def test_that_it_returns_a_valid_number(self):
      mock = MockUserInput([3])
      validator = InputValidator(mock)
      self.assertEqual(3,validator.validate((1,2,3)))

  def test_that_it_returns_a_number_in_valid_response(self):
      valid_responses = [3,4,5]
      mock = MockUserInput((1,4))
      validator = InputValidator(mock)
      self.assertEqual(4,validator.validate(valid_responses))

  def test_that_it_works_with_str_nums(self):
      valid_responses = (3,4)
      input_source = MockUserInput("3")
      validator = InputValidator(input_source)
      self.assertEqual(3,validator.validate(valid_responses))

  def test_that_it_works_through_different_types(self):
      valid_response = [7]
      input_source = MockUserInput(["a","b","7"])
      validator = InputValidator(input_source)
      self.assertEqual(7,validator.validate(valid_response))

  def test_that_it_returns_different_types(self):
      valid_responses = ["a","b"]
      input_source = MockUserInput(["c","d","b"])
      validator = InputValidator(input_source)
      self.assertEqual("b",validator.validate(valid_responses,str))
