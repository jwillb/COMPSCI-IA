from tkinter import *

def calcClayWindow(mainWindow):
	ROOT = Tk()
	ROOT.title("Clayculator")
	ROOT.geometry("225x245")
	ROOT.resizable(False, False)

	OPTIONS = ["M350","M69", "M420"] # will be real options later

	CIRCLE = IntVar()
	SQUARE = IntVar()
	
	CLAY_CHOICE = StringVar()

	FRAME = Frame(ROOT, padx=5, pady=5)
	FRAME.pack()

	SHAPE_LABEL = Label(FRAME, text="Shape of object:", font=("Arial", 11))
	SHAPE_LABEL.grid(row=0, column=0, sticky=W, columnspan=2)

	CIRCLE_CHECK = Checkbutton(FRAME)
	CIRCLE_CHECK.grid(row=1, column=0, sticky=E)

	CIRCLE_LABEL = Label(FRAME, text="Circle")
	CIRCLE_LABEL.grid(row=1, column=1, sticky=W+S)

	SQUARE_CHECK = Checkbutton(FRAME)
	SQUARE_CHECK.grid(row=2, column=0, sticky=E)

	SQUARE_LABEL = Label(FRAME, text="Square")
	SQUARE_LABEL.grid(row=2, column=1, sticky=W+S)

	SEPARATOR_1 = Label(FRAME, text=" ")
	SEPARATOR_1.grid(row=3, column=0)

	DIMENSION_LABEL = Label(FRAME, text="Final Side Length/Circumference:", font=("Arial", 11))
	DIMENSION_LABEL.grid(row=4, column=0, sticky=W, columnspan=3)

	DIMENSION_TEXTBOX = Entry(FRAME, width=6)
	DIMENSION_TEXTBOX.grid(row=5, column=0, columnspan=1, sticky=E)

	CM_LABEL = Label(FRAME, text="cm")
	CM_LABEL.grid(row=5, column=1, sticky=W)

	CLAY_LABEL = Label(FRAME, text="Type of clay:")
	CLAY_LABEL.grid(row=6, column=0)

	CLAY_OPTIONS = OptionMenu(FRAME, CLAY_CHOICE, *OPTIONS)
	CLAY_OPTIONS.grid(row=7, column=0, sticky=W)
	
	ROOT.mainloop()

if __name__ == "__main__":
	calcClayWindow("Ain't got no main window")
