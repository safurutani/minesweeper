from tkinter import Button

class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Text'
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