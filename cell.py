from tkinter import Button
import random

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
            text=f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.lmb_actions)
        btn.bind('<Button-3>', self.rmb_actions)
        self.cell_btn_object = btn
    def lmb_actions(self, event):
        print(event)
        print("I got left clicked!")
    def rmb_actions(self, event):
        print(event)
        print("I got right clicked!")

    @staticmethod
    def randomize_mines(): 
        mines = random.sample(Cell.all, 9)
        for picked_cell in mines:
            picked_cell.is_mine = True
    def __repr__(self):
        return f"Cell ({self.x}, {self.y})"
