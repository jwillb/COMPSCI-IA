from tkinter import *
from tkinter.messagebox import showerror, showinfo
from add_clay import addClayWindow
from calc_clay import calcClayWindow
from pathlib import Path
import backend

def mainWindow():
    FIRST_RUN = True

    FILENAME = "clays.db"
    if (Path.cwd() / FILENAME).exists():
        FIRST_RUN = False

    if FIRST_RUN:
        backend.createTable(FILENAME)
    
    ROOT = Tk()
    ROOT.resizable(False, False)
    ROOT.title("")

    CHOICE = IntVar(ROOT, 2)

    TITLE = Label(ROOT, text="Select mode:", padx=100, pady=20, font=("Arial", 15))
    TITLE.grid(row=0, column=0, columnspan=3)

    CALC_CHOICE = Radiobutton(ROOT, text="Calculate shrinkage of a pot", variable=CHOICE, value=2)
    ADD_CHOICE = Radiobutton(ROOT, text="Add a new clay type", variable=CHOICE, value=1)

    CALC_CHOICE.grid(row=1, column=0, columnspan=2, sticky=W)
    ADD_CHOICE.grid(row=2, column=0, columnspan=2, sticky=W)

    SPACER = Label(ROOT, text=" ")
    SPACER.grid(row=3, column=0)

    def okPressed():
        if CHOICE.get() == 1:
            ROOT.destroy()
            addClayWindow(mainWindow)
        else:
            ROOT.destroy()
            calcClayWindow(mainWindow)

    CONFIRM_BTN = Button(ROOT, text="Ok", width=28, command=okPressed, pady="5")
    CONFIRM_BTN.grid(row=4, column=1)

    SPACER_2 = Label(ROOT, text=" ")
    SPACER_2.grid(row=5, column=0)

    ROOT.mainloop()

if __name__ == "__main__":
    mainWindow()
