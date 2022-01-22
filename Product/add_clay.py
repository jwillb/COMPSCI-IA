from tkinter import *
from tkinter.messagebox import showerror
from re import search
import backend

def addClayWindow(mainWindow):
    # Most of this is the same as first_screen.py and delete_clay.py
    ROOT = Tk()
    ROOT.title("Add a new clay type")
    ROOT.geometry("225x265")
    ROOT.resizable(False, False)

    FRAME = Frame(ROOT, padx=5, pady=2)
    FRAME.pack()

    NAME_LABEL = Label(FRAME, text="Name of clay:", font=("Arial", 11), padx=0, pady=5)
    NAME_LABEL.grid(row=0, column=0, sticky=W)

    NAME_ENTRY = Entry(FRAME, width=20)
    NAME_ENTRY.grid(row=1, column=0, sticky=N+S+E+W)

    SHRINK_LABEL = Label(FRAME, text="Shrinkage rate:", font=("Arial", 11), padx=0, pady=5)
    SHRINK_LABEL.grid(row=2, column=0, sticky=W)

    SHRINK_ENTRY = Entry(FRAME, width=20)
    SHRINK_ENTRY.grid(row=3, column=0, sticky=N+S+E+W)

    PERCENT_1 = Label(FRAME, text="%")
    PERCENT_1.grid(row=3, column=2, sticky=W)

    ABSORPTION_LABEL = Label(FRAME, text="Absorption rate:", font=("Arial", 11), padx=0, pady=5)
    ABSORPTION_LABEL.grid(row=4, column=0, sticky=W)

    ABSORPTION_ENTRY = Entry(FRAME, width=20)
    ABSORPTION_ENTRY.grid(row=5, column=0, sticky=N+S+E+W)

    PERCENT_2 = Label(FRAME, text="%")
    PERCENT_2.grid(row=5, column=2, sticky=W)

    SEPARATOR = Label(FRAME, text=" ")
    SEPARATOR.grid(column=0, row=6)

    def addClay(): # Adds a clay with the user inputted information into the database, with invalid input checking
        CLAY_NAME = NAME_ENTRY.get()
        try:
            SHRINK_RATE = float(SHRINK_ENTRY.get())
            ABSORB_RATE = float(ABSORPTION_ENTRY.get())
            if not search("[a-zA-Z]", CLAY_NAME):
                raise ValueError
            backend.addToTable("clays.db", CLAY_NAME, SHRINK_RATE, ABSORB_RATE)
            NAME_ENTRY.delete(0, END)
            SHRINK_ENTRY.delete(0, END)
            ABSORPTION_ENTRY.delete(0, END)
        except ValueError:
            showerror(message="You seem to have entered an incorrect input. Please try again.")
        

    ADD_BUTTON = Button(FRAME, text="Add!", width=16, command=addClay)
    ADD_BUTTON.grid(row=7, column=0, sticky=E)

    SEPARATOR_2 = Label(FRAME, text=" ")
    SEPARATOR_2.grid(column=0, row=8)

    def goBack():
        ROOT.destroy()
        mainWindow()

    RETURN_BUTTON = Button(FRAME, text="Return", width=4, command=goBack)
    RETURN_BUTTON.grid(row=9, column=0, sticky=W)

    ROOT.mainloop()

if __name__ == "__main__":
    print("Wrong file")
