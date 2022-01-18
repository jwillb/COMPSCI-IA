from tkinter import *
from tkinter.messagebox import showerror, showinfo
from add_clay import addClayWindow

def mainWindow():
	ROOT = Tk()
	ROOT.resizable(False, False)
	ROOT.title("")

	ADD = IntVar()
	CALC = IntVar()

	def flipCalc():
		if ADD.get():
			CALC.set(0)
		else:
			CALC.set(1)

	def flipAdd():
		if CALC.get():
			ADD.set(0)
		else:
			ADD.set(1)

	TITLE = Label(ROOT, text="Select mode:", padx=100, pady=20, font=("Arial", 15))
	TITLE.grid(row=0, column=0, columnspan=3)

	CALC_CLAY = Checkbutton(ROOT, padx=10, pady=10, variable=CALC, onvalue=1, offvalue=0, command=flipAdd)
	CALC_CLAY.grid(row=1, column=0)

	CALC_LABEL = Label(ROOT, text="Calculate shrinkage of a pot", padx=5)
	CALC_LABEL.grid(row=1, column=1, columnspan=2, sticky=W)

	ADD_CLAY = Checkbutton(ROOT, padx=10, pady=10, variable=ADD, onvalue=1, offvalue=0, command=flipCalc)
	ADD_CLAY.grid(row=2, column=0)

	ADD_LABEL = Label(ROOT, text="Add a new clay type", padx=5)
	ADD_LABEL.grid(row=2, column=1, columnspan=1, sticky=W)

	SPACER = Label(ROOT, text=" ")
	SPACER.grid(row=3, column=0)

	def okPressed():
		if (not ADD.get()) and (not CALC.get()):
			showerror(title="Input error", message="You need to select an option.")
		elif ADD.get():
			ROOT.destroy()
			addClayWindow(mainWindow)

	CONFIRM_BTN = Button(ROOT, text="Ok", width=14, command=okPressed)
	CONFIRM_BTN.grid(row=4, column=1, sticky=W)

	ROOT.mainloop()

if __name__ == "__main__":
	mainWindow()
