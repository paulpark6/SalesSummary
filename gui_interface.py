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

    def create_widgets(self):
        #"""Create three buttons"""
        #Create first buttom
        btn1 = Button(self.master, text = "I do nothing")
        btn1.pack()

        #Create second button
        btn2 = Button(self.master, text = "T do nothing as well")
        btn2.pack()

        #Create third button
        btn3=Button(self.master, text = "I do nothing as well as well")
        btn3.pack()






