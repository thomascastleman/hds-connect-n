
import game
import re

class Human(game.ConnectNGame):

	def __init__(self, _symbol):
		self.symbol = _symbol

	def getMove(self, state):
		print "Num of cols: ", len(state.board[0])
		while True:
			move = raw_input("Enter column number: ")
			# protect against non numeric input
			if not bool(re.search('[^0-9]', move)):
				move = int(move)
				# check move legality
				if move in range(0, len(state.board[0])):
					break
		return move
		