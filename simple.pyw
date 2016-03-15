#!/usr/bin/python3

from tkinter import *
import math

class Calc:
	def __init__(self,master):

		#checkers
		self.multidigit = 0
		self.space = 0

		#frames
		self.display_frame = Frame(master)
		self.display_frame.grid(row=0,column=0,columnspan=2)

		self.input_frame = Frame(master)
		self.input_frame.grid(row=1,column=0,columnspan=2)

		self.operator_frame = Frame(master)
		self.operator_frame.grid(row=2,column=0)

		self.toggle_frame = Frame(master)
		self.toggle_frame.grid(row=2,column=1)

		#display 
		self.display = Label(self.display_frame,text="",font=("Courier",14,"bold"),height=1,width=32,anchor="e",relief="sunk",borderwidth=6)
		self.display.grid(row=0,column=0)

		#keypad
		keyfont = ("Sans-Serif",13,"bold")

		inputs = [str(i) for i in range(1,10)] + ["0","."]
		operators = ["%","÷","π","x","-","+","e","log","logx","ln","sin","cos","tan","x!","x^y"]
		toggles = ["C","+/-","="]

		for i in range(len(inputs)):
			number = Button(self.input_frame,text=inputs[i],font=keyfont,bg="#e0e0d1",height=2,width=5,relief="ridge",borderwidth=3,command=lambda:self.input(inputs[i]))
			if i < 6:
				number.grid(row=0,column=i)
			else:
				if inputs[i] == "0":
					number.config(width=11)
					number.grid(row=1,column=3,columnspan=2)
				elif inputs[i] == ".":
					number.config(bg="#b4fc9c")
					number.grid(row=1,column=5)
				else:
					number.grid(row=1,column=i-6)

		for i in range(len(operators)):
			operator = Button(self.operator_frame,text=operators[i],font=keyfont,bg="#a3cfdc",height=2,width=5,relief="ridge",borderwidth=3,command=lambda:self.operate(operators[i]))
			if i < 5:
				operator.grid(row=0,column=i)
			elif i < 10:
				operator.grid(row=1,column=i-5)
			else:
				operator.grid(row=2,column=i-10)

		for i in range(len(toggles)):
			toggle = Button(self.toggle_frame,text=toggles[i],font=keyfont,bg="#b4fc9c",height=2,width=5,relief="ridge",borderwidth=3,command=lambda:self.toggle(toggles[i]))
			toggle.grid(row=i,column=0)


	def input(self,number):
		print("input")
		return

	def operate(self,operator):
		print("operate")
		return

	def toggle(self,toggle):
		print("toggle")
		return

#create root
root = Tk()

Calculator = Calc(root)
#mainloop
root.mainloop()