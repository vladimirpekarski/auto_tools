# -*- coding: utf-8 -*-
from Tkinter import *


class Quiter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT)

if __name__ == '__main__':
    Quiter().mainloop()