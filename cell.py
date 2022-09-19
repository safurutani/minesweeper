from tkinter import Button,Label
from tkinter import font
import random
import settings
import ctypes
import sys

class Cell:
    all=[]
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT
    def __init__(self,x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_open = False
        self.is_flagged = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #append obj to the cell.all list
        Cell.all.append(self)
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=6,
            height=2,
            text=f''
        )
        btn.bind('<Button-1>', self.lmb_actions)
        btn.bind('<Button-3>', self.rmb_actions)
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg="#777AAA",
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=3,
            font=('Berlin Sans FB', 20)
        )
        Cell.cell_count_label_object = lbl

    def lmb_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            #clears all surrounding cells when no mines are near
            if self.nearby_mines == 0:
                for cell_obj in self.adjacent_cells:
                    if not self.is_flagged:
                        cell_obj.show_cell()
                    self.cell_btn_object.unbind('<Button-1>')
                    self.cell_btn_object.unbind('<Button-3>')
            if not self.is_flagged:
                self.show_cell()
                #cancel lmb and rmb events when cell is opened
                self.cell_btn_object.unbind('<Button-1>')
                self.cell_btn_object.unbind('<Button-3>')
            if Cell.cell_count == settings.NUM_MINES:
                ctypes.windll.user32.MessageBoxW(0, "Congratulations! You avoided all the mines!", "You Won!,", 0)
        
    def rmb_actions(self, event):
        if not self.is_flagged:
            self.cell_btn_object.configure(bg="#3C5468")
            self.is_flagged = True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_flagged = False
    #should end game - shows red temporarily
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "You clicked on a mine :(", "Game Over", 0)
        sys.exit()    
    #return a cell obj based on val of x,y
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def adjacent_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x,     self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x,     self.y + 1),
        ]
        #eliminate none values in the list
        cells = [cell for cell in cells if cell is not None]
        return cells

    #needs to utilize algorithm to determine # of adjacent mines
    @property
    def nearby_mines(self):
        counter = 0
        for cell in self.adjacent_cells:
            if cell.is_mine:
                counter += 1
        return counter
    
    #looks at the 8 adjacent cells
    def show_cell(self): 
        if not self.is_open:
            #decrease cell count by one each time one is clicked  
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.nearby_mines,font=('Berlin Sans FB', 10))
            #Update the cell count when cells are clicked
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells Left: {Cell.cell_count}")
        #lets game know that the cell has been revealed to user
        self.is_open = True
    
    @staticmethod
    def randomize_mines(): 
        mines = random.sample(Cell.all, settings.NUM_MINES)
        for picked_cell in mines:
            picked_cell.is_mine = True
    def __repr__(self):
        return f"Cell ({self.x}, {self.y})"
