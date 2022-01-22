from tkinter import *
from tkinter.messagebox import showerror, showinfo
from add_clay import addClayWindow
from calc_clay import calcClayWindow
from delete_clay import deleteClayWindow
from pathlib import Path
import backend

def mainWindow(): # Window is a function in order to be called later when the user wants to go back to the main window
    FIRST_RUN = True

    FILENAME = "clays.db"
    if (Path.cwd() / FILENAME).exists(): # Check if the database exists
        FIRST_RUN = False

    if FIRST_RUN:
        backend.createTable(FILENAME) # Create the database if it doesn't exist
    
    ROOT = Tk() # Create the Tkinter instance/window
    ROOT.resizable(False, False) # Stop the user from resizing the window to maintain the visibility of all of the buttons
    ROOT.title("") # Set the title to blank because it's not needed

    CHOICE = IntVar(ROOT, 2) # Create a Tkinter integer variable, as Tkinter buttons can only be used with Tkinter variables.
                             # It is set at two so that the calculation function is selected first.

    TITLE = Label(ROOT, text="Select mode:", padx=100, pady=20, font=("Arial", 15))
    TITLE.grid(row=0, column=0, columnspan=3)

    CALC_CHOICE = Radiobutton(ROOT, text="Calculate shrinkage of a pot", variable=CHOICE, value=2) # Buttons to select window
    ADD_CHOICE = Radiobutton(ROOT, text="Add a new clay type", variable=CHOICE, value=1)
    DELETE_CHOICE = Radiobutton(ROOT, text="Delete a clay type", variable=CHOICE, value=3)

    CALC_CHOICE.grid(row=1, column=0, columnspan=2, sticky=W) # Place window buttons into window
    ADD_CHOICE.grid(row=2, column=0, columnspan=2, sticky=W)
    DELETE_CHOICE.grid(row=3, column=0, columnspan=2, sticky=W)

    SPACER = Label(ROOT, text=" ") # An ad-hoc separator to space out widgets
    SPACER.grid(row=4, column=0)

    def okPressed(): # Destroy the window and open the window specified, called when confirm button is pressed
        if CHOICE.get() == 1:
            ROOT.destroy()
            addClayWindow(mainWindow)
        elif CHOICE.get() == 2:
            ROOT.destroy()
            calcClayWindow(mainWindow)
        else:
            ROOT.destroy()
            deleteClayWindow(mainWindow)

    CONFIRM_BTN = Button(ROOT, text="Ok", width=28, command=okPressed, pady="5")
    CONFIRM_BTN.grid(row=5, column=1)

    SPACER_2 = Label(ROOT, text=" ")
    SPACER_2.grid(row=6, column=0)

    ROOT.mainloop()

if __name__ == "__main__": # Only execute the main window if called by the user
    mainWindow()
