class Homescreen:

	def __init__(self, screen):

		self.screen = screen

		self.player1Algorithm = None
		self.player1Piece = None

		self.player2Algorithm = None
		self.player2Piece = None

		from Button import Button
		import constants

		self.player1Text = Button(screen, (constants.BUTTON_HEIGHT, constants.BUTTON_HEIGHT), "Player 1", outline=False)
		self.player2Text = Button(screen, (constants.SCREEN_HEIGHT - 3 * constants.BUTTON_HEIGHT, constants.BUTTON_HEIGHT), "Player 2", outline=False)

		self.player1AlgoButtons = [
			Button(screen, (self.player1Text.getBottomUp()[0], self.player1Text.getBottomUp()[1] + constants.BETWEEN_BUTTONS_Y_SPACE), "human"),
			Button(screen, (self.player1Text.getBottomUp()[0], self.player1Text.getBottomUp()[1] + 2 * constants.BETWEEN_BUTTONS_Y_SPACE), "minimax"),
			Button(screen, (self.player1Text.getBottomUp()[0], self.player1Text.getBottomUp()[1] + 3 * constants.BETWEEN_BUTTONS_Y_SPACE), "alpha-beta")
		]

		self.player1PiecesButtons = [
			Button(screen, (self.player1Text.getBottomUp()[0], self.player1Text.getBottomUp()[1] + 4 * constants.BETWEEN_BUTTONS_Y_SPACE), "dogs"),
			Button(screen, (self.player1Text.getBottomUp()[0], self.player1Text.getBottomUp()[1] + 5 * constants.BETWEEN_BUTTONS_Y_SPACE), "jaguar")
		]

		self.player2AlgoButtons = [
			Button(screen, (self.player2Text.getBottomUp()[0], self.player2Text.getBottomUp()[1] + constants.BETWEEN_BUTTONS_Y_SPACE), "human"),
			Button(screen, (self.player2Text.getBottomUp()[0], self.player2Text.getBottomUp()[1] + 2 * constants.BETWEEN_BUTTONS_Y_SPACE), "minimax"),
			Button(screen, (self.player2Text.getBottomUp()[0], self.player2Text.getBottomUp()[1] + 3 * constants.BETWEEN_BUTTONS_Y_SPACE), "alpha-beta")
		]

		self.player2PiecesButtons = [
			Button(screen, (self.player2Text.getBottomUp()[0], self.player2Text.getBottomUp()[1] + 4 * constants.BETWEEN_BUTTONS_Y_SPACE), "dogs"),
			Button(screen, (self.player2Text.getBottomUp()[0], self.player2Text.getBottomUp()[1] + 5 * constants.BETWEEN_BUTTONS_Y_SPACE), "jaguar")
		]

		left = self.player1PiecesButtons[1].getBottomUp()
		right = self.player2PiecesButtons[1].getBottomUp()

		left = (left[0] + constants.BUTTON_HEIGHT + (right[0] - left[0] - 2 * constants.BUTTON_HEIGHT) // 2, left[1] + constants.BUTTON_WIDTH)

		self.startButton = Button(screen, left, "start", outline = True)

	def draw(self):

		self.player1Text.draw()
		self.player2Text.draw()

		for button in self.player1AlgoButtons:
			button.draw()

		for button in self.player2AlgoButtons:
			button.draw()

		for button in self.player1PiecesButtons:
			button.draw()

		for button in self.player2PiecesButtons:
			button.draw()

		self.startButton.draw()

	def getPressed(self, clickCoords):

		import constants

		for button in self.player1AlgoButtons:
			if button.pressed(clickCoords):
				button.setColor(constants.GREEN)
				text = button.getText()

				if text == "human":
					self.player1AlgoButtons[1].setColor(constants.WHITE)
					self.player1AlgoButtons[2].setColor(constants.WHITE)
				elif text == "minimax":
					self.player1AlgoButtons[0].setColor(constants.WHITE)
					self.player1AlgoButtons[2].setColor(constants.WHITE)
				else:
					self.player1AlgoButtons[0].setColor(constants.WHITE)
					self.player1AlgoButtons[1].setColor(constants.WHITE)

		for button in self.player2AlgoButtons:
			if button.pressed(clickCoords):
				button.setColor(constants.GREEN)
				text = button.getText()

				if text == "human":
					self.player2AlgoButtons[1].setColor(constants.WHITE)
					self.player2AlgoButtons[2].setColor(constants.WHITE)
				elif text == "minimax":
					self.player2AlgoButtons[0].setColor(constants.WHITE)
					self.player2AlgoButtons[2].setColor(constants.WHITE)
				else:
					self.player2AlgoButtons[0].setColor(constants.WHITE)
					self.player2AlgoButtons[1].setColor(constants.WHITE)

		for button in self.player1PiecesButtons:
			if button.pressed(clickCoords):
				button.setColor(constants.GREEN)
				text = button.getText()

				if text == "dogs":
					self.player1PiecesButtons[1].setColor(constants.WHITE)
					self.player2PiecesButtons[1].setColor(constants.GREEN)
					self.player2PiecesButtons[0].setColor(constants.WHITE)
				else:
					self.player1PiecesButtons[0].setColor(constants.WHITE)
					self.player2PiecesButtons[0].setColor(constants.GREEN)
					self.player2PiecesButtons[1].setColor(constants.WHITE)

		for button in self.player2PiecesButtons:
			if button.pressed(clickCoords):
				button.setColor(constants.GREEN)
				text = button.getText()

				if text == "dogs":
					self.player2PiecesButtons[1].setColor(constants.WHITE)
					self.player1PiecesButtons[1].setColor(constants.GREEN)
					self.player1PiecesButtons[0].setColor(constants.WHITE)
				else:
					self.player2PiecesButtons[0].setColor(constants.WHITE)
					self.player1PiecesButtons[0].setColor(constants.GREEN)
					self.player1PiecesButtons[1].setColor(constants.WHITE)

	def run(self):

		import pygame, constants

		for event in pygame.event.get():

			self.screen.fill(constants.WHITE)
			self.draw()

			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
				return False
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					clickCoords = event.pos
					print(self.getPressed(clickCoords))



		pygame.display.flip()

		return True