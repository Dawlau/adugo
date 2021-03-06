BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (211, 211, 211)
GREEN = (0, 255, 0)

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 800

BUTTON_HEIGHT = SCREEN_HEIGHT // 8
BUTTON_WIDTH = SCREEN_WIDTH // 20
BETWEEN_BUTTONS_Y_SPACE = BUTTON_WIDTH + BUTTON_WIDTH // 2

SQUARE_LENGTH = SCREEN_WIDTH // 7
SQUARE_SIDE_WIDTH = 5

CIRCLE_RADIUS = 25

# DEFAULT_GRID = [
# 	['d', 'd', 'd', 'd', 'd'],
# 	['d', 'd', 'd', 'd', 'd'],
# 	['d', 'd', 'j', 'd', 'd'],
# 	[None, None, None, None, None],
# 	[None, None, None, None, None],
# 	[None, None, None, None, None],
# 	[None, None, None, None, None],
# ]

DEFAULT_GRID = [
	['j', 'd', 'd', 'd', 'd'],
	['d', 'd', 'd', 'd', 'd'],
	[None, 'd', 'd', 'd', 'd'],
	[None, None, None, None, None],
	[None, None, None, None, None],
	[None, None, None, None, None],
	[None, None, None, None, None],
]

ADJACENCY_LIST = [
	[1, 5, 6], # 0
	[0, 2, 6], # 1
	[1, 3, 6, 7, 8], # 2
	[2, 4, 8], # 3
	[3, 8, 9], # 4
	[0, 6, 10], # 5
	[0, 1, 2, 5, 7, 10, 11, 12], # 6
	[2, 6, 8, 12], # 7
	[2, 3, 4, 7, 9, 12, 13, 14], # 8
	[4, 8, 14], # 9
	[5, 6, 11, 15, 16], # 10
	[6, 10, 12, 16], # 11
	[6, 7, 8, 11, 13, 16, 17, 18], # 12
	[8, 12, 14, 18], # 13
	[8, 9, 13, 18, 19], # 14
	[10, 16, 20], # 15
	[10, 11, 12, 15, 17, 20, 21, 22], # 16
	[12, 16, 18, 22], # 17
	[12, 13, 14, 17, 19, 22, 23, 24], # 18
	[14, 18, 24], # 19
	[15, 16, 21], # 20
	[16, 20, 22], # 21
	[16, 17, 18, 21, 23, 26, 27, 28], # 22
	[18, 22, 24], # 23
	[18, 19, 23], # 24
	[], # 25
	[22, 27, 30], # 26
	[22, 26, 28, 32], # 27
	[22, 27, 34], # 28
	[], # 29
	[26, 31], # 30
	[30, 32], # 31
	[27, 31, 33], # 32
	[32, 34], # 33
	[28, 33], # 34
]