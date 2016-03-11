#!/usr/bin/python

from tkinter import *
from math import sqrt


root = Tk()

titleframe = Frame(root, height=20,width=100,borderwidth=5,bg="")
titleframe.grid(row=0,column=0,columnspan=2)

title = Label(titleframe, text="CIRCLE GRAPH CALCULATOR",anchor=CENTER)
title.grid(row=0,column=0)
title2 = Label(titleframe, text="x^2 + y^2 + ax + by + c = 0", anchor=CENTER)
title2.grid(row=1,column=0)

entryframe = Frame(root,height=100,width=50,borderwidth=5)
entryframe.grid(row=1,column=0)

displayframe = Frame(root, height=100,width=130,borderwidth=5)
displayframe.grid(row=1,column=1)

a_label = Label(entryframe, text="A", borderwidth=10)
a_label.grid(row=0,column=0)
a_input = Entry(entryframe, borderwidth=5,width=10)
a_input.grid(row=0,column=1)

b_label = Label(entryframe, text="B", borderwidth=10)
b_label.grid(row=1,column=0)
b_input = Entry(entryframe, borderwidth=5,width=10)
b_input.grid(row=1,column=1)

c_label = Label(entryframe, text="C", borderwidth=10)
c_label.grid(row=2,column=0)
c_input = Entry(entryframe, borderwidth=5,width=10)
c_input.grid(row=2,column=1)


is_circle_label = Label(displayframe, text="Is Circle: ",borderwidth=10,width=10,anchor=W)
is_circle_label.grid(row=0,column=0)
is_circle_display = Label(displayframe, text="None",borderwidth=10,width=30,anchor=E)
is_circle_display.grid(row=0,column=1)

radius_label = Label(displayframe, text="Radius: ",borderwidth=10,width=10,anchor=W)
radius_label.grid(row=1,column=0)
radius_display = Label(displayframe, text="None",borderwidth=10,width=30,anchor=E)
radius_display.grid(row=1,column=1)

center_label = Label(displayframe, text="Center Point: ", borderwidth=10,width=10,anchor=W)
center_label.grid(row=2,column=0)
center_display = Label(displayframe,text="None",borderwidth=10,width=30,anchor=E)
center_display.grid(row=2,column=1)

equation_label = Label(displayframe, text="Equation: ", borderwidth=10, width=10, anchor=W)
equation_label.grid(row=3,column=0)
equation_display = Label(displayframe,text="None",borderwidth=10,width=30,anchor=E)
equation_display.grid(row=3,column=1)


def calculate():
	if a_input.get() and b_input.get() and c_input.get():
		try:
			a = int(a_input.get())
			b = int(b_input.get())
			c = int(c_input.get())
		except ValueError:
			is_circle_display.config(text="Value Error.")
			a_input.delete(0,'end')
			b_input.delete(0,'end')
			c_input.delete(0,'end')
			return
		c = (-1 * c) #x^2 + y^2 +ax + by = +/- c
		# (x^2 + ax) + (y^2 + bx) = c
		half_a = (a/2)
		half_b = (b/2)
		c = (c) + ((half_a**2) + (half_b**2))
		# (x +/- a/2)^2 + (y +/- b/2)^2 = (c + (a/2)^2 + (b/2)^2)
		equation = "(x+{})^2 + (y+{})^2 = {}".format(half_a,half_b,c)
		center = "({},{})".format((-1*half_a),(-1*half_b))
		if c < 0:
			c = (-1 * c)
			radius = str(sqrt(c)) + " i"
			is_circle = "False"
		elif c == 0:
			radius = "0"
			is_circle = "False"
		else:
			radius = str(sqrt(c))
			is_circle = "True"
		is_circle_display.config(text=is_circle)
		radius_display.config(text=radius)
		center_display.config(text=center)
		equation_display.config(text=equation)
		return
	else:
		return

def clearinput():
	a_input.delete(0,'end')
	b_input.delete(0,'end')
	c_input.delete(0,'end')
	is_circle_display.config(text="None")
	radius_display.config(text="None")
	center_display.config(text="None")
	equation_display.config(text="None")
	return


submit = Button(entryframe, borderwidth=3, text="SUBMIT", command = calculate, anchor=CENTER)
submit.grid(row=3,column=0)
clear = Button(entryframe,borderwidth=3, text="CLEAR",command = clearinput, anchor=CENTER)
clear.grid(row=3,column=1)

root.mainloop()
