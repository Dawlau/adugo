# adugo

Global constants:

```
WIDTH, HEIGHT, CIRCLE_RADIUS, SQUARE_LENGTH, DEFAULT_GRID, GRAY, BLACK
```


## Grid drawing:


```
- create matrix of 7x5 representing the game table
- each cell in the matrix will be a tuple ((character, selected); 'j' - for jaguar, 'd' - for dog and None for nothing)
- map grid cell to number and reversed
- create adjancency list for the grid
- create matrix for on screen positions
- create "Draw segment" function that draws a segment between a pair of grid cells
(for circles use dx, dy differences to move the segment from origin to outside; to calculate dx, dy you should check where the second cell is relative to the first: up, down, left, right)

- if the value is 'j' or 'd' draw the respective circles (first step)
- draw the segments (based on adjancency list)
```

## Game logic:

```
- for jaguar jumps keep a variable called "turns" that won't decrement if the jaguar jumped
- a move is considered done when "turns" is 0
- for minimax and alpha beta, the next state is given by the board after a legal move
```

## Game interaction:

```
- when a player clicks on the screen get the click coordinates and check if the player clicked on a valid piece and if a piece is charged (before selecting a piece, unselect all the other pieces), wait for a click on another valid piece (in case the computer selected a piece place a timeout before actually moving the piece)
- while in game, if the player presses backspace, go back to home screen
```

## Needed classes:

```
App
Homescreen
Game
Grid
Player
Ai
```
