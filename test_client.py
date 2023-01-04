from tkinter import *
import pandas as pd
import gui_interface as g


root = Tk()
root.title("Lazy Button 2")
root.geometry("500x500")
app = g(root)
things = ["wef", "wef", "we"]
app.create_dropdown(things)
root.mainloop()