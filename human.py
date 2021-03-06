
import re	# regex to match non numeric chars

class Human:

	def __init__(self, _name, _symbol):
		self.name = _name
		self.symbol = _symbol
		self.game = None	# reference to game that contains this human

	def getMove(self, state):
		while True:
			move = raw_input("Enter column number: ")
			# protect against empty strings, non numeric input, and illegal moves
			if len(move) > 0 and not bool(re.search('[^0-9]', move)) and state.checkMoveLegality(int(move)):
				break
		return int(move)