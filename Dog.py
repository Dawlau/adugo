from Utilities import Utilities


class Dog:

	def __init__(self):
		import constants, copy
		self.adjacencyList = copy.deepcopy(constants.ADJACENCY_LIST)

	def isValid(self, grid, cell):
		i, j = cell
		if i == None or j == None:
			return False
		return grid[i][j] == 'd'

	def makeMove(self, grid, selected, cell):

		from Utilities import Utilities

		node = Utilities.cellToNode(grid, selected)
		nextNode = Utilities.cellToNode(grid, cell)

		if nextNode in self.adjacencyList[node] and grid[cell[0]][cell[1]] is None:
			grid[selected[0]][selected[1]], grid[cell[0]][cell[1]] = grid[cell[0]][cell[1]], grid[selected[0]][selected[1]]
			return 0

		return 1