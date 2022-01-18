from tkinter import *
import backend

def calcClayWindow(mainWindow):
	ROOT = Tk()
	ROOT.title("Clayculator")
	ROOT.geometry("225x275")
	ROOT.resizable(False, False)

	OPTIONS = ["M350","M69", "M420", "MMMMMM"] # will be real options later

	CHOICE = IntVar(ROOT, 1)
	
	CLAY_CHOICE = StringVar()

	FRAME = Frame(ROOT, padx=5, pady=5)
	FRAME.pack()

	SHAPE_LABEL = Label(FRAME, text="Shape of object", font=("Arial", 11))
	SHAPE_LABEL.grid(row=0, column=0, columnspan=2, sticky=W)

	CIRCLE_BUTTON = Radiobutton(FRAME, text="Circle", variable=CHOICE, value=1)
	CIRCLE_BUTTON.grid(row=1, column=0, sticky=W)

	SQUARE_BUTTON = Radiobutton(FRAME, text="Square", variable=CHOICE, value=2)
	SQUARE_BUTTON.grid(row=2, column=0, sticky=W)

	SEPARATOR_1 = Label(FRAME, text=" ")
	SEPARATOR_1.grid(row=3, column=0)

	DIMENSION_LABEL = Label(FRAME, text="Final Side Length/Circumference:", font=("Arial", 11))
	DIMENSION_LABEL.grid(row=4, column=0, sticky=W, columnspan=3)

	DIMENSION_TEXTBOX = Entry(FRAME, width=6)
	DIMENSION_TEXTBOX.grid(row=5, column=0, columnspan=1, sticky=W)

	CM_LABEL = Label(FRAME, text="(cm)")
	CM_LABEL.grid(row=5, column=2, sticky=E)

	CLAY_LABEL = Label(FRAME, text="Type of clay:", font=("Arial", 11))
	CLAY_LABEL.grid(row=6, column=0, sticky=W)

	CLAY_OPTIONS = OptionMenu(FRAME, CLAY_CHOICE, *OPTIONS)
	CLAY_OPTIONS.grid(row=7, column=0, sticky=W)

	def calcClay():
		pass
	
	SEPARATOR_2 = Label(FRAME, text=" ")
	SEPARATOR_2.grid(row=8, column=0)
	
	CALC_BUTTON = Button(FRAME, text="Calculate!", width=5)
	CALC_BUTTON.grid(row=9, column=0, sticky=E+W, columnspan=3)

	SEPARATOR_3 = Label(FRAME, text=" ")
	SEPARATOR_3.grid(row=10)

	def goBack():
		ROOT.destroy()
		mainWindow()

	RETURN_BUTTON = Button(FRAME, text="Return", command=goBack)
	RETURN_BUTTON.grid(row=11, column=0, sticky=W)
	
	ROOT.mainloop()

if __name__ == "__main__":
	calcClayWindow("Ain't got no main window")
