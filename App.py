class App:

	def __init__(self):

		import pygame
		import constants

		pygame.init()
		self.screen = pygame.display.set_mode([constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH])
		pygame.display.set_caption("Andrei Blahovici Adugo")

		self.running = True

	def run(self):

		from Game import Game

		game = Game(self.screen)

		while self.running:
			self.running = game.run()