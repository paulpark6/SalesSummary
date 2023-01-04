from tkinter import *

# grab from database
OPTIONS = [
"Jan",
"Feb",
"Mar"
]

master = Tk()
master.geometry("280x200")
variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def selected():
    print ("value is:" + variable.get())

button = Button(master, text="Select", command=selected)
button.pack()

mainloop()


