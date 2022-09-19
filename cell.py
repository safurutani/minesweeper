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
            width=6,
            height=2,
            text=f''
        )
        btn.bind('<Button-1>', self.lmb_actions)
        btn.bind('<Button-3>', self.rmb_actions)
        self.cell_btn_object = btn
    
    def lmb_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:self.show_cell()
    def rmb_actions(self, event):
        print("rmb")
   
    #should end game - shows red temporarily
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")

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
        self.cell_btn_object.configure(text=self.nearby_mines)        

    @staticmethod
    def randomize_mines(): 
        mines = random.sample(Cell.all, settings.NUM_MINES)
        for picked_cell in mines:
            picked_cell.is_mine = True
        print(mines)
    def __repr__(self):
        return f"Cell ({self.x}, {self.y})"
