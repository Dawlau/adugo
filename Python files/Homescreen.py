from Player import Player

'''
This class takes care of the homescreen flow
'''
class Homescreen:

	def __init__(self, screen):

		self.screen = screen

		from Button import Button
		import constants

		self.player1Text = Button(screen, (constants.BUTTON_HEIGHT, constants.BUTTON_HEIGHT), "Player 1", outline=False)
		self.player2Text = Button(screen, (constants.SCREEN_HEIGHT - 3 * constants.BUTTON_HEIGHT, constants.BUTTON_HEIGHT), "Player 2", outline=False)

		self.player1 = None
		self.player2 = None

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

	def drawState0(self):

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

	def getPressed(self, clickCoords): # if a button was clicked set colors

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

	def pickUpParameters(self): # if the user pressed the start button get the parameters

		import constants
		from Player import Player
		from Ai import Ai

		player1Algo = ""
		player2Algo = ""

		if self.player1AlgoButtons[0].getColor() == constants.GREEN:
			player1Algo = "human"
		elif self.player1AlgoButtons[1].getColor() == constants.GREEN:
			player1Algo = "minimax"
		elif self.player1AlgoButtons[2].getColor() == constants.GREEN:
			player1Algo = "alpha-beta"

		if self.player2AlgoButtons[0].getColor() == constants.GREEN:
			player2Algo = "human"
		elif self.player2AlgoButtons[1].getColor() == constants.GREEN:
			player2Algo = "minimax"
		elif self.player2AlgoButtons[2].getColor() == constants.GREEN:
			player2Algo = "alpha-beta"

		from Dog import Dog
		from Jaguar import Jaguar

		if player1Algo != "" and player2Algo != "":
			if self.player1PiecesButtons[0].getColor() == constants.GREEN:

				if player1Algo == "human":
					self.player1 = Player(Dog())
				elif player1Algo != "":
					self.player1 = Ai(Dog(), player1Algo)

				if player2Algo == "human":
					self.player2 = Player(Jaguar())
				elif player2Algo != "":
					self.player2 = Ai(Jaguar(), player2Algo)

			elif self.player1PiecesButtons[1].getColor() == constants.GREEN:

				if player1Algo == "human":
					self.player1 = Player(Jaguar())
				elif player1Algo != "":
					self.player1 = Ai(Jaguar(), player1Algo)

				if player2Algo == "human":
					self.player2 = Player(Dog())
				elif player2Algo != "":
					self.player2 = Ai(Dog(), player2Algo)

	def runState0(self): # choose algorithm and piece to play with

		import pygame, constants

		for event in pygame.event.get():

			self.screen.fill(constants.WHITE)
			self.drawState0()

			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
				return ("exit", self.player1, self.player2)
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					clickCoords = event.pos
					self.getPressed(clickCoords)
					if self.startButton.pressed(clickCoords):
						self.pickUpParameters()
						for button in self.player1AlgoButtons:
							button.setColor(constants.WHITE)

						for button in self.player2AlgoButtons:
							button.setColor(constants.WHITE)

		pygame.display.flip()

		return ("homescreen", self.player1, self.player2)

	def drawState1(self): # choose difficulty for Ai

		import constants
		from Ai import Ai

		self.screen.fill(constants.WHITE)


		if isinstance(self.player1, Ai):
			self.player1Text.draw()

			self.player1AlgoButtons[0].setText("easy")
			self.player1AlgoButtons[1].setText("medium")
			self.player1AlgoButtons[2].setText("hard")

			for button in self.player1AlgoButtons:
				button.draw()


		if isinstance(self.player2, Ai):
			self.player2Text.draw()

			self.player2AlgoButtons[0].setText("easy")
			self.player2AlgoButtons[1].setText("medium")
			self.player2AlgoButtons[2].setText("hard")

			for button in self.player2AlgoButtons:
				button.draw()

			self.startButton.draw()

	def state1_checkPressed(self, clickCoords): # if button was pressed in the second state

		import constants
		from Ai import Ai

		if isinstance(self.player1, Ai):
			for button in self.player1AlgoButtons:
				if button.pressed(clickCoords):
					button.setColor(constants.GREEN)
					text = button.getText()

					if text == "easy":
						self.player1AlgoButtons[1].setColor(constants.WHITE)
						self.player1AlgoButtons[2].setColor(constants.WHITE)
					elif text == "medium":
						self.player1AlgoButtons[0].setColor(constants.WHITE)
						self.player1AlgoButtons[2].setColor(constants.WHITE)
					else:
						self.player1AlgoButtons[0].setColor(constants.WHITE)
						self.player1AlgoButtons[1].setColor(constants.WHITE)



		if isinstance(self.player2, Ai):
			for button in self.player2AlgoButtons:
				if button.pressed(clickCoords):
					button.setColor(constants.GREEN)
					text = button.getText()

					if text == "easy":
						self.player2AlgoButtons[1].setColor(constants.WHITE)
						self.player2AlgoButtons[2].setColor(constants.WHITE)
					elif text == "medium":
						self.player2AlgoButtons[0].setColor(constants.WHITE)
						self.player2AlgoButtons[2].setColor(constants.WHITE)
					else:
						self.player2AlgoButtons[0].setColor(constants.WHITE)
						self.player2AlgoButtons[1].setColor(constants.WHITE)

	def setDifficulties(self):

		from Ai import Ai
		import constants

		if isinstance(self.player1, Ai):

			if self.player1AlgoButtons[0].getColor() == constants.GREEN:
				self.player1.setDifficulty("easy")
			elif self.player1AlgoButtons[1].getColor() == constants.GREEN:
				self.player1.setDifficulty("medium")
			elif self.player1AlgoButtons[2].getColor() == constants.GREEN:
				self.player1.setDifficulty("hard")

		if isinstance(self.player2, Ai):

			if self.player2AlgoButtons[0].getColor() == constants.GREEN:
				self.player2.setDifficulty("easy")
			elif self.player2AlgoButtons[1].getColor() == constants.GREEN:
				self.player2.setDifficulty("medium")
			elif self.player2AlgoButtons[2].getColor() == constants.GREEN:
				self.player2.setDifficulty("hard")


	def runState1(self):

		import pygame, constants

		for event in pygame.event.get():

			self.screen.fill(constants.WHITE)
			self.drawState1()

			if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
				return "exit", self.player1, self.player2
			else:
				if event.type == pygame.MOUSEBUTTONDOWN:
					clickCoords = event.pos
					self.state1_checkPressed(clickCoords)

					if self.startButton.pressed(clickCoords):
						self.setDifficulties()
						return "game", self.player1, self.player2


		pygame.display.flip()

		return "homescreen", self.player1, self.player2

	def run(self):

		import pygame

		if self.player1 is None:
			return self.runState0()
		else:
			if isinstance(self.player1, Player) and isinstance(self.player2, Player):
				return "game", self.player1, self.player2
			return self.runState1()