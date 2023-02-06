# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:39:23 2023

@author: User
"""

from tkinter import *
import random

root=Tk()
root.title("password Generator")
root.geometry("400x400")

label = Label(root)

array_3d = [[['1','2','3','4','5','6'],["head","tail"],["A","B","C","D","E","F","G","H"]]]
print(array_3d[0][2][3])

def new_password():
    random_no_1 = random.randint(0,5)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)
    
    letter1 = str(array_3d[0][0][random_no_1])
    letter2 = (array_3d[0][1][random_no_2])
    letter3 = (array_3d[0][2][random_no_3])
    label["text"] = letter1 + "" + letter2 + "" + letter3
    
btn = Button(root, text="new password", command = new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

label.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    
root.mainloop()
    
    