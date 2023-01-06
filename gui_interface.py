from tkinter import * 
import pandas as pd

class gui(Frame):
    def __init__(self,master):
        self.master = master

    def create_dropdown(self, data):
        #self.data = data
        variable = StringVar(self.master)
        variable.set(data[0]) # default value
        w = OptionMenu(self.master, variable, *data)
        w.pack()

    def create_textInput(self, title = "title", height = 5, width = 20):
        # adding new label
        text = Text(self.master, height, width)
        text.pack()
        
    def exit(self):
        btn1 = Button(self.master, text = "quit?", command=self.master.destroy)
        btn1.pack()





