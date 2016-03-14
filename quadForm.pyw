#!/usr/bin/python

from tkinter import *
from math import sqrt

root = Tk()

title_frame = Frame(root)
title_frame.grid(row=0,column=0)

input_frame = Frame(root)
input_frame.grid(row=1,column=0)

display_frame = Frame(root)
display_frame.grid(row=2,column=0)

title = Label(title_frame,text="Quadratic Formula",borderwidth=0,font=("Sans-Serif",16),anchor="center")
title.grid(row=0,column=0)
description = Label(title_frame,text="ax^2 + bx + c = 0",borderwidth=0,font=("Sans-Serif",14),anchor="center")
description.grid(row=1,column=0)

label_font = ("Courier",14,"bold")
input_font = ("Courier",13)

a_label = Label(input_frame,text="A:",borderwidth=0,font=label_font,anchor="e")
a_label.grid(row=0,column=0)
a_input = Entry(input_frame,borderwidth=3,font=input_font,relief="sunk",width=10)
a_input.grid(row=0,column=1)

b_label = Label(input_frame,text="B:",borderwidth=0,font=label_font,anchor="e")
b_label.grid(row=0,column=2)
b_input = Entry(input_frame,borderwidth=3,font=input_font,relief="sunk",width=10)
b_input.grid(row=0,column=3)

c_label = Label(input_frame,text="C:",borderwidth=0,font=label_font,anchor="e")
c_label.grid(row=0,column=4)
c_input = Entry(input_frame,borderwidth=3,font=input_font,relief="sunk",width=10)
c_input.grid(row=0,column=5)

root_one_frame = Frame(display_frame)
root_one_frame.grid(row=1,column=0)

root_two_frame = Frame(display_frame)
root_two_frame.grid(row=1,column=1)

root_one_label = Label(root_one_frame,text="Root 1",font=("Courier",14,"underline"),relief="flat",anchor="center")
root_one_label.grid(row=0,column=0)
root_one_display = Label(root_one_frame,text="0",font=("Courier",14,"bold"),relief="ridge",anchor="center")
root_one_display.grid(row=1,column=0)

root_two_label = Label(root_two_frame,text="Root 2",font=("Courier",14,"underline"),relief="flat",anchor="center")
root_two_label.grid(row=0,column=0)
root_two_display = Label(root_two_frame,text="0",font=("Courier",14,"bold"),relief="ridge",anchor="center")
root_two_display.grid(row=1,column=0)

def calculate():
	if a_input.get() and b_input.get() and c_input.get() and a_input.get() != "0":
		try:
			a,b,c = int(a_input.get()), int(b_input.get()), int(c_input.get())
		except ValueError:
			return

		# -(b)  +/-  /b^2 - 4(a)(c)|
		# __________________________
		#           2(a)
		
		d = ((b**2) - (4*a*c))
		if d < 0:
			d = round(sqrt(-1*d),3)
			root_one = "({} + {})/({})".format((-1*b),(str(d)+"i"),(2*a))
			root_two = "({} - {})/({})".format((-1*b),(str(d)+"i"),(2*a))
		else:
			d = round(sqrt(d),3)
			root_one = str(((-1*b)+d)/(2*a))
			root_two = str(((-1*b)-d)/(2*a))

		root_one_display.config(text=root_one)
		root_two_display.config(text=root_two)

		return

	else:
		return

def clear():
	root_one_display.config(text="0")
	root_two_display.config(text="0")
	a_input.delete(0,"end")
	b_input.delete(0,"end")
	c_input.delete(0,"end")

	return

submit_button = Button(display_frame,text="SUBMIT",relief="raised",command=calculate,anchor="center")
submit_button.grid(row=0,column=0)
clear_button = Button(display_frame,text="CLEAR",relief="raised",command=clear,anchor="center")
clear_button.grid(row=0,column=1)

root.mainloop()