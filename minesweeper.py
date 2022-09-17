from tkinter import *
import settings
import utils

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
    height=utils.height_percent(20)
)
top_frame.place(x=0, y=0)

#keeps window open until closed out with the X
root.mainloop()