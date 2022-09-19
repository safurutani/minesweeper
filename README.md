# minesweeper
Generates a square grid of the designated size with randomized placement of mines that the user needs to avoid clicking.
If one mine gets clicked, the game is over.
When left clicked, cells will reveal a number that indicates how many mines are within the surrounding 8 cells of the original cell. If the cell has no surrounding mines, the game will automatically reveal the numbers of those cells for the user to save them time.
Users can right click cells to flag them as potential mines. Doing so will prevent them from being able to click on the cell so the game doesn't potentially end. 
Right clicking the flagged cell will undo this so the user can click on the cell again in case it was an accident or they realize it wasn't a mine after all.
Clicking on/revealing all the cells that weren't mines causes the player to win the game.
As the user clicks cells, they can see how many cells are left available for them to click.