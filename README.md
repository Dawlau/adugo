# adugo

Global constants:

```
WIDTH, HEIGHT, CIRCLE_RADIUS, SQUARE_LENGTH, DEFAULT_GRID
```


## Grid drawing:


```
- create matrix of 7x5 representing the game table
- each cell in the matrix will have a value ('j' - for jaguar, 'd' - for dog and None for nothing)
- map grid cell to number and reversed
- create adjancency list for the grid
- create matrix for on screen positions
- create "Draw segment" function that draws a segment between a pair of grid cells
(for circles use dx, dy differences to move the segment from origin to outside; to calculate dx, dy you should check where the second cell is relative to the first: up, down, left, right)

- if the value is 'j' or 'd' draw the respective circles (first step)
- draw the segments
```