# -*- coding: utf-8 -*-

from Tkinter import *
from idlelib import AutoComplete
from idlelib import AutoCompleteWindow


class Example(Frame):
    def __init__(self, parent=None, text=''):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        text = Text(self, relief=SUNKEN)
        text.pack()
        self.text = text
        self.indentwidth = '4.0'
        self.tabwidth = '4.0'
        self.context_use_ps1 = '0.0'
        ac = AutoComplete.AutoComplete(self)
        text.bind("<Tab>", ac.autocomplete_event)




Example().mainloop()

