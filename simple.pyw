#! python3

from tkinter import *
import math

class Calc:
	def __init__(self,master):

		#checkers
		self.multidigit = False
		self.space = 0
		self.operand_one = None
		self.current_operator = None
		self.operand_two = None
		self.decimal = False

		#display
		self.result_string = ""

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
		self.display = Label(self.display_frame,text=self.result_string,font=("Courier",14,"bold"),height=1,width=32,anchor="e",relief="sunk",borderwidth=6)
		self.display.grid(row=0,column=0)

		#keypad
		keyfont = ("Sans-Serif",13,"bold")

		inputs = [str(i) for i in range(1,10)] + ["0","."]
		operators = ["+","-","*","÷","e"] + ["x!","x^y","ln","%","π"] + ["logx","log","sin","cos","tan"]

		toggles = ["C","+/-","="]

		for i in range(len(inputs)):
			n = inputs[i]
			if n is ".":
				number = Button(self.input_frame,text=n,font=keyfont,bg="#b4fc9c",height=2,width=5,relief="ridge",borderwidth=3,command=lambda n=n:self.toggle(n))
			else:
				number = Button(self.input_frame,text=n,font=keyfont,bg="#e0e0d1",height=2,width=5,relief="ridge",borderwidth=3,command=lambda n=n:self.input(n))
			if i < 6:
				number.grid(row=0,column=i)
			else:
				if n is "0":
					number.config(width=11)
					number.grid(row=1,column=3,columnspan=2)
				elif n is ".":
					number.grid(row=1,column=5)
				else:
					number.grid(row=1,column=i-6)

		for i in range(len(operators)):
			o = operators[i]
			operator = Button(self.operator_frame,text=o,font=keyfont,bg="#a3cfdc",height=2,width=5,relief="ridge",borderwidth=3,command=lambda o=o:self.operate(o))
			if i < 5:
				operator.grid(row=0,column=i)
			elif i < 10:
				operator.grid(row=1,column=i-5)
			else:
				operator.grid(row=2,column=i-10)

		for i in range(len(toggles)):
			t = toggles[i]
			toggle = Button(self.toggle_frame,text=t,font=keyfont,bg="#b4fc9c",height=2,width=5,relief="ridge",borderwidth=3,command=lambda t=t:self.toggle(t))
			toggle.grid(row=i,column=0)


	def input(self,number):
		if self.space is 0:
			if self.multidigit is False:
				self.operand_one = str(number)
				self.multidigit = True
			else: 
				if self.decimal is True:
					x = str(self.operand_one) + "." + str(number)
					self.decimal = False
				else:
					x = str(self.operand_one) + str(number)
				self.operand_one = (x)
			self.result_string = str(self.operand_one)
			self.display.config(text=self.result_string)
		else:
			if self.multidigit is False:
				self.operand_two = str(number)
				self.multidigit = True
			else:
				if self.decimal is True:
					x = str(self.operand_two) + "." + str(number)
					self.decimal = False
				else:
					x = str(self.operand_two) + str(number)
				self.operand_two = str(x)
			self.result_string = str(self.operand_two)
			self.display.config(text=self.result_string)

		return

	def operate(self,operator):
		self.multidigit = False
		if operator is "÷":
			self.current_operator = "/"
		elif operator is "%":
			if self.space is 0:
				self.operand_one = round(float(self.operand_one),2)
			else:
				self.operand_two = round(float(self.operand_two),2)
		elif operator is "x^y":
			self.current_operator = "**"
		elif operator is "e":
			if self.space is 0:
				self.operand_one = "2.71828182845"
				self.result_string = self.operand_one
			else:
				self.operand_two = "2.71828182845"
				self.result_string = self.operand_two
			self.display.config(text="e")
		elif operator is "π":
			if self.space is 0:
				self.operand_one = "3.14159265358979"
				self.result_string = self.operand_one
			else:
				self.operand_two = "3.14159265358979"
				self.result_string = self.operand_two
			self.display.config(text="π")
		else:
			self.current_operator = operator
		self.space = 1
		return

	def toggle(self,toggle):
		if toggle is ".":
			self.decimal = True
		elif toggle is "=":
			easy_ones = ["+","-","*","/","**"]
			if self.current_operator in easy_ones:
				self.result_string = str(eval(self.operand_one+self.current_operator+self.operand_two))
				self.display.config(text=self.result_string)
				self.operand_one = self.result_string
				self.space = 0
				multidigit = False
			else:
				pass
		elif toggle is "C":

			self.multidigit = False
			self.space = 0
			self.operand_one = None
			self.current_operator = None
			self.operand_two = None
			self.decimal = False
			self.result_string = ""
			self.display.config(text=self.result_string)

		elif toggle is "+/-":
			if self.space is 0:
				self.operand_one = str(-1*int(self.operand_one))
				self.result_string = self.operand_one
				self.display.config(text=self.operand_one)
			else:
				self.operand_two = str(-1*int(self.operand_two))
				self.result_string = self.operand_two
				self.display.config(text=self.operand_two)
		
		return

#create root
root = Tk()

Calculator = Calc(root)
#mainloop
root.mainloop()