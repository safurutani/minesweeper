from tkinter import Button
import random
import settings

class Cell:
    all=[]
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #append obj to the cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f''
        )
        btn.bind('<Button-1>', self.lmb_actions)
        btn.bind('<Button-3>', self.rmb_actions)
        self.cell_btn_object = btn
    def lmb_actions(self, event):
        if self.is_mine:
            self.show_mine()
    #ends game - player loses
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
    def rmb_actions(self, event):
        print("rmb")    

    @staticmethod
    def randomize_mines(): 
        mines = random.sample(Cell.all, settings.NUM_MINES)
        for picked_cell in mines:
            picked_cell.is_mine = True
        print(mines)
    def __repr__(self):
        return f"Cell ({self.x}, {self.y})"
