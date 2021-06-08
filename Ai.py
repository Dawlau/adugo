class Ai:

	def __init__(self, piece, algorithm, difficulty = "easy", heuristic = 1):

		self.turns = 0
		self.piece = piece
		self.algorithm = algorithm
		self.difficulty = difficulty
		self.heuristic = heuristic


	def selectPiece(self, grid, cell):
		return self.piece.isValid(grid, cell)

	def makeMove(self, grid):

		from State import State
		state, score = self.minimax(State(grid, None, None), self.piece, 4, max)

		return state

	def minimax(self, state, piece, depth, f, alpha = -500, beta = 500):

		if depth == 0:
			return state, piece.eval(state)

		nextStates = piece.genMoves(state.getGrid())

		from Jaguar import Jaguar
		from Dog import Dog
		import copy

		nextPiece = Jaguar() if isinstance(piece, Dog) else Dog()
		bestScore, nextF = (float('-inf'), min) if f == max else (float('inf'), max)
		bestState = None

		for nextState in nextStates:

			_, aux = self.minimax(nextState[-1], nextPiece, depth - 1, nextF)
			a = f(aux, bestScore)

			if a != bestScore:
				bestScore = a
				bestState = copy.deepcopy(nextState)

		return bestState, bestScore


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