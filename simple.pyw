#!/usr/bin/python3

from tkinter import *
import math

#create root
root = Tk()

#frames
display_frame = Frame(root)
display_frame.grid(row=0,column=0)

input_frame = Frame(root)
input_frame.grid(row=1,column=0)

#display 
display = Label(display_frame,text="0",font=("Courier",14,"bold"),height=1,width=20,anchor="e")
display.grid(row=0,column=0)

#keypad



#mainloop
root.mainloop()