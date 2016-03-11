#!/usr/bin/python

from tkinter import *
import os

root = Tk()

titleframe = Frame(root, borderwidth=5,relief=GROOVE,width=60,bg="blue")
titleframe.grid(row=0,column=0,columnspan=3,rowspan=2)

menuframe = Frame(root,borderwidth=3,width=60,bg="black")
menuframe.grid(row=2,column=0,columnspan=3,rowspan=4)

title_font = ('System',16)
title = Label(titleframe,text="Calculator Menu",\
				borderwidth=5,anchor=CENTER,width=60,bg="#00e6ac",font=title_font)
title.grid(row=0,column=0,columnspan=3)
author = Label(titleframe,text="James Crovo",\
				borderwidth=5,anchor=CENTER,width=60,bg="#00e6ac",font=title_font)
author.grid(row=1,column=0,columnspan=3)

def runpro(program):
	os.system("py {}.pyw".format(program))
	return

button_font = ('System', 12)
simpleCalc = Button(menuframe,text="Simple\n Calculator",command=lambda:runpro("simple"),borderwidth=5,width=21,bg="#8cb3d9")
simpleCalc.grid(row=0,column=0)

circleGraph = Button(menuframe,text="Circle\n Graph",command=lambda:runpro("circleGraph"),borderwidth=5,width=21,bg="#8cb3d9")
circleGraph.grid(row=0,column=1)

quadForm = Button(menuframe,text="Quad.\n Form.",command=lambda:runpro("quadForm"),borderwidth=5,width=21,bg="#8cb3d9")
quadForm.grid(row=0,column=2)

root.mainloop()
