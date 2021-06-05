class Ai:

	def __init__(self, piece, algorithm, difficulty = "easy", heuristic = 1):

		self.turns = 0
		self.piece = piece
		self.algorithm = algorithm
		self.difficulty = difficulty
		self.heuristic = heuristic

	def selectPiece(self, grid, cell):
		return self.piece.isValid(grid, cell)

	def makeMove(self, grid, selected, cell):
		return self.piece.makeMove(grid, selected, cell)

	def setDifficulty(self, difficulty):
		self.difficulty = difficulty

	def setHeuristic(self, heuristic):
		self.heuristic = heuristic

	def getPieceType(self):

		from Dog import Dog
		from Jaguar import Jaguar

		if isinstance(self.piece, Dog):
			return "dog"
		else:
			return "jaguar"