import sys
sys.path.append("../")
from test_utils import MockUserInput, MockPlayer
from board import Board
import unittest
from playerinput import InputValidator, MoveValidator

class MoveValidatorTests(unittest.TestCase):

  def test_that_it_returns_a_valid_number(self):
      mock = MockUserInput([3])
      mock_player = MockPlayer("x",mock)
      validator = MoveValidator()
      self.assertEqual(3,validator.validate(mock_player,(1,2,3)))

  def test_that_it_returns_a_number_in_valid_response(self):
      valid_responses = [3,4,5]
      mock = MockUserInput((1,4))
      mock_player = MockPlayer("x",mock)
      validator = MoveValidator()
      self.assertEqual(4,validator.validate(mock_player,valid_responses))

  def test_that_it_works_with_str_nums(self):
      valid_responses = (3,4)
      input_source = MockUserInput("3")
      mock_player = MockPlayer("x",input_source)
      validator = MoveValidator()
      self.assertEqual(3,validator.validate(mock_player,valid_responses))

  def test_that_it_works_through_different_types(self):
      valid_response = [7]
      input_source = MockUserInput(["a","b","7"])
      mock_player = MockPlayer("x",input_source)
      validator = MoveValidator()
      self.assertEqual(7,validator.validate(mock_player,valid_response))

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
 