import board
import player
import ai

class Game(object):

  def run(self):
      game_board = board.Board()
      token = self.capture_input(('x','o'),"Would you like to be x or o: ")
      human = player.Player(token)
      computer = ai.AI(human.opponent_token)
      turn = self.capture_input((1,2),"Would you like to move first or second (1,2): ",int)
      turn_map = {1:self.human_first, 2:self.computer_first}
      turn_map[turn](game_board,human,computer)
      print game_board
      winner = game_board.winner()
      if winner:
          print winner + " wins!"
      else:
          print "It's a tie!"
      self.play_again()

  def human_first(self,board,human,computer):
      while not board.game_over():
          move = self.user_move(board)
          board.make_move(move,human.token)
          self.computer_move_if_not_game_over(board,computer)
          self.render_board_if_not_over(board)

  def computer_first(self,board,human,computer):
      while not board.game_over():
          self.computer_move_if_not_game_over(board,computer)
          self.render_board_if_not_over(board)
          if board.game_over():
              break
          move = self.user_move(board)
          board.make_move(move,human.token)
          self.render_board_if_not_over(board)

  def user_move(self, board):
      print board.available_moves()
      move = self.capture_input(board.available_moves(),"Please select a move: ",int)
      return move

  def computer_move_if_not_game_over(self,board,comp_player):
      if not board.game_over():
          move = comp_player.best_move(board)
          board.make_move(move,comp_player.token)

  def render_board_if_not_over(self,board):
      if not board.game_over():
          print board

  def play_again(self):
      answer = self.capture_input(('y','n'),"Would you like to play again: ")
      if answer == 'y':
          self.run()

  def capture_input(self,responses,prompt,data_type=str):
      answer = 0
      while answer not in responses:
          try:
              answer = data_type(raw_input(prompt))
          except:
              continue
      return answer