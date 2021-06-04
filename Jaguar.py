class Jaguar:

	def __init__(self):
		import constants, copy
		self.adjacencyList = copy.deepcopy(constants.ADJACENCY_LIST)

	def isValid(self, grid, cell):
		i, j = cell
		if i == None or j == None:
			return False
		return grid[i][j] == 'j'

	def makeMove(self, grid, selected, cell):

		from Utilities import Utilities

		node = Utilities.cellToNode(grid, selected)
		nextNode = Utilities.cellToNode(grid, cell)

		if nextNode in self.adjacencyList[node] and grid[cell[0]][cell[1]] is None:
			grid[selected[0]][selected[1]], grid[cell[0]][cell[1]] = grid[cell[0]][cell[1]], grid[selected[0]][selected[1]]
			return 0

		if nextNode:

			dr = Utilities.sign(selected[0] - cell[0])
			dc = Utilities.sign(selected[1] - cell[1])

			intermediateCell = (cell[0] + dr, cell[1] + dc)
			intermediateNode = Utilities.cellToNode(grid, intermediateCell)

			i1, j1 = selected
			i2, j2 = intermediateCell
			i3, j3 = cell

			if grid[i2][j2] == 'd' and grid[i3][j3] is None and intermediateNode in self.adjacencyList[node] and nextNode in self.adjacencyList[intermediateNode]:
				grid[i1][j1], grid[i3][j3] = grid[i3][j3], grid[i1][j1]
				grid[i2][j2] = None

			return 1

		return 0
