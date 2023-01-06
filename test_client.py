from tkinter import *
import pandas as pd
import gui_interface


root = Tk()
root.title("DataSet")
root.geometry("500x500")
app = gui_interface.gui(root)

# import data with pandas
things = ["wef", "wef", "we"]
app.create_dropdown(things)
app.create_textInput()
app.exit()
root.mainloop()