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
center_frame.place(x=utils.width_percent(5), y=utils.height_percent(20))

c1 = Cell()
c1.create_btn_object(center_frame)
c1.cell_btn_object.place(
    x=0, y=0
)

#keeps window open until closed out with the X
root.mainloop()