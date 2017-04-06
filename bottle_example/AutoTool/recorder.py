import os
import sys
from Tkinter import *
from AutoTool.classes.Quiter import Quiter
from ScrolledText import ScrolledText
from AutoTool.classes.CustomAutoComplete import CustomAutoComplete


class RecorderIDE(Frame):
    title = 'Recorder'

    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.master.title(RecorderIDE.title)
        self.make_widgets()
        self.set_text()

    @property
    def auto_file(self):
        return os.path.join(os.curdir, 'test.txt')

    @property
    def is_auto_file_exists(self):
        return os.path.exists(self.auto_file)

    @property
    def file_state(self):
        return os.stat(self.auto_file).st_mtime

    def make_widgets(self):
        # need for AutoComplete
        self.indentwidth = '0'
        self.tabwidth = '0'
        self.context_use_ps1 = '0'
        scrolled_text = ScrolledText(self, relief=SOLID)
        scrolled_text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.text = scrolled_text
        auto_complete = CustomAutoComplete(self)
        scrolled_text.bind("<Tab>", auto_complete.autocomplete_event)
        self.quiter = Quiter(self)

    def set_text(self):
        if self.is_auto_file_exists:
            self.init_file_state = self.file_state
            with open(self.auto_file) as auto_file:
                content = auto_file.read()
                self.text.insert(END, content)
                self.text.see(END)
            self.follow_auto_file()

    def follow_auto_file(self):
        if self.init_file_state != self.file_state:
            with open(self.auto_file) as auto_file:
                content = auto_file.readlines()
                self.text.insert(END, content[-1] + '\n')
                self.text.see(END)
            self.init_file_state = self.file_state
        self.text.after(100, self.follow_auto_file)




if __name__ == '__main__':
    RecorderIDE().mainloop()
