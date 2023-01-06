import pandas as pd
import gui_interface
from tkinter import *

data = pd.read_csv('./DataBase/price_list_AUG.csv')
produits = data[data['produits'].str.contains('10W-40')]
sub_data = produits.loc[:,['code','produits', 'litrage']]

codes = sub_data['code'].tolist()
products = sub_data['produits'].tolist()
literages = sub_data['litrage'].tolist()

data_list = list()
for i in range(len(codes)):
    str = codes[i] + "\t" + products[i] + "\t" + literages[i]
    data_list.append(str)

print(data_list)

root =Tk()
root.title("DataSet")
root.geometry("500x500")
app = gui_interface.gui(root)


app.create_dropdown(data_list)
app.exit()
root.mainloop()
