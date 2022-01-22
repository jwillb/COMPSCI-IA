from tkinter import *
from tkinter.messagebox import showerror, showinfo
import backend

def calcClayWindow(mainWindow):
    # Most of this is similar to first_screen.py, other than the database accessing
    FILENAME = "clays.db"

    OPTIONS = backend.getClays(FILENAME)

    ROOT = Tk()
    ROOT.title("Clayculator") # Bad pun
    ROOT.geometry("235x295")
    ROOT.resizable(False, False)

    OPTIONS = backend.getClays(FILENAME)

    CHOICE = IntVar(ROOT, 1)

    CLAY_CHOICE = StringVar()

    FRAME = Frame(ROOT, padx=5, pady=5)
    FRAME.pack()

    # Various elements and buttons

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

    SEPARATOR_2 = Label(FRAME, text=" ")
    SEPARATOR_2.grid(row=8, column=0)

    def calcButton(): # Use all of the data supplied to calculate the shrinkage and show a message box to the user
                      # when the button is pressed, or show an error
        try:
            ID = backend.fetchClay("clays.db", CLAY_CHOICE.get())
            SHRINK_RATE = backend.getShrink("clays.db", ID)
            NEW_DIMENSION = backend.calcShrink(SHRINK_RATE, float(DIMENSION_TEXTBOX.get()))
            MESSAGE = backend.genText(NEW_DIMENSION, float(DIMENSION_TEXTBOX.get()), CHOICE.get(), SHRINK_RATE)
            showinfo(title="Result", message=MESSAGE)
        except ValueError:
            showerror(message="You need to enter a proper dimension value. Please try again.")
        

    CALC_BUTTON = Button(FRAME, text="Calculate!", width=5, command=calcButton)
    CALC_BUTTON.grid(row=9, column=0, sticky=E+W, columnspan=3)

    SEPARATOR_3 = Label(FRAME, text=" ")
    SEPARATOR_3.grid(row=10)

    def goBack(): # Goes back to the main window, while first destroying the current window
        ROOT.destroy()
        mainWindow()

    RETURN_BUTTON = Button(FRAME, text="Return", command=goBack)
    RETURN_BUTTON.grid(row=11, column=0, sticky=W)

    ROOT.mainloop()

if __name__ == "__main__": # Only works properly if the program is launched by first_screen.py
    print("Wrong file")
