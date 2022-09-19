from tkinter import *
import settings
import utils
from cell import Cell

#creates the window
root = Tk()
root.configure(bg="#A5C9EA")
#size of the window and ability for user to readjust
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False, False)
#title of window
root.title("Minesweeper")

top_frame = Frame(
    root, 
    bg="#777AAA",
    width=800,
    height=utils.height_percent(15)
)
top_frame.place(x=0, y=0)

center_frame = Frame(
    root,
    bg="#C2EAFC",
    width=utils.width_percent(90),
    height=utils.height_percent(75)
)
center_frame.place(x=utils.width_percent(4.5), y=utils.height_percent(20))

#dynamically add all the cells as buttons into the frame
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
            )
#calling the label from Cell class
Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(x=600, y=15)
Cell.randomize_mines()

#keeps window open until closed out with the X
root.mainloop()