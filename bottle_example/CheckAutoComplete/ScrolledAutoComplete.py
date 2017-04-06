# -*- coding: utf-8 -*-

from Tkinter import *
from idlelib.AutoComplete import AutoComplete

from AutoTool.classes.Quiter import Quiter


class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.make_widgets()
        self.set_text(text, file)
        self.indentwidth = '0'
        self.tabwidth = '0'
        self.context_use_ps1 = '0'

    def make_widgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)
        text.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = text
        ac = CustomAutoComplete(self)
        text.bind("<Tab>", ac.autocomplete_event)
        # text.bind("<Key>", ColorDelegator().toggle_colorize_event)

        quiter = Quiter(self)


    def set_text(self, text='', file=None):
        if file:
            text = open(file).read()
        # self.text.delete('1.0', END)
        # self.text.insert('1.0', text)
        # self.text.mark_set(INSERT, '1.0')
        # self.text.focus()


class CustomAutoComplete(AutoComplete):
    def fetch_completions(self, what, mode):
        if what == "":
            return ['test', 'test2'], ['test', 'test2']
        else:
            return ['sub1', 'sub2'], ['sub2', 'sub3']


if __name__ == '__main__':
    root = Tk()
    ScrolledText(root, text='Check')
    root.mainloop()