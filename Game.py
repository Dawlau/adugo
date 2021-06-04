class Game:

	def __init__(self, screen):

		import copy, constants
		from Player import Player
		from Jaguar import Jaguar
		from Dog import Dog

		self.screen = screen
		self.screen.fill(constants.WHITE)

		self.grid = copy.deepcopy(constants.DEFAULT_GRID)
		self.adjacencyList = copy.deepcopy(constants.ADJACENCY_LIST)
		self.selected = (None, None)

		self.players = [Player(Jaguar()), Player(Dog())]
		self.turn = 0

		self.mapCoordinates()

	def mapCoordinates(self):

		import constants

		self.onScreenCoordinates = []

		row = [(constants.SCREEN_HEIGHT // 5, constants.SCREEN_WIDTH // 15)]
		for i in range(1, len(self.grid[0])):
			row.append((row[i - 1][0] + constants.SQUARE_LENGTH, row[i - 1][1]))

		self.onScreenCoordinates.append(row)

		for i in range(1, len(self.grid)):
			for j in range(len(self.grid[i])):
				if j == 0:
					row = [(row[0][0], row[0][1] + constants.SQUARE_LENGTH)]
				else:
					row.append((row[j - 1][0] + constants.SQUARE_LENGTH, row[j - 1][1]))
				if j == len(self.grid[i]) - 1:
					self.onScreenCoordinates.append(row)



	def drawGrid(self):

		import pygame, constants
		from Utilities import Utilities

		# draw segments
		for node in range(len(self.grid) * len(self.grid[0])):
			for nextNode in self.adjacencyList[node]:
				i1, j1 = Utilities.nodeToCell(self.grid, node)
				i2, j2 = Utilities.nodeToCell(self.grid, nextNode)

				x = self.onScreenCoordinates[i1][j1]
				y = self.onScreenCoordinates[i2][j2]

				pygame.draw.line(self.screen, constants.BLACK, x, y, constants.SQUARE_SIDE_WIDTH)

		for node in range(len(self.grid) * len(self.grid[0])): # draw pieces

			i, j = Utilities.nodeToCell(self.grid, node)

			if self.grid[i][j] == 'j':

				center = self.onScreenCoordinates[i][j]
				radius = constants.CIRCLE_RADIUS

				if self.selected == (i, j):
					pygame.draw.circle(self.screen, constants.RED, center, radius)
				pygame.draw.circle(self.screen, constants.BLACK, center, radius - 2)


			elif self.grid[i][j] == 'd':

				center = self.onScreenCoordinates[i][j]
				radius = constants.CIRCLE_RADIUS

				if self.selected == (i, j):
					pygame.draw.circle(self.screen, constants.RED, center, radius)
				pygame.draw.circle(self.screen, constants.GRAY, center, radius - 2)




	def run(self):

		import pygame, constants
		from Ai import Ai
		from Utilities import Utilities

		for event in pygame.event.get():

			self.screen.fill(constants.WHITE)

			endGame = Utilities.endGame(self.grid)
			if endGame is not None:
				print(endGame)
				return False

			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
				return False
			else:

				if isinstance(self.players[self.turn], Ai):
					pass
				elif event.type == pygame.MOUSEBUTTONDOWN:
					clickCoords = event.pos

					row, col = Utilities.clickCoordsToCell(self.onScreenCoordinates, self.grid, clickCoords)

					selected = self.players[self.turn].selectPiece(self.grid, (row, col))
					if selected:
						self.selected = (row, col)
					else: # actual move
						if row is not None and col is not None and self.selected != (None, None):
							leftTurns = self.players[self.turn].makeMove(self.grid, self.selected, (row, col))

							if leftTurns == 0:
								self.turn ^= 1


			self.drawGrid()

		pygame.display.flip()

		return True