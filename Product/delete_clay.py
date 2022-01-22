from tkinter import *
import backend

def deleteClayWindow(mainWindow):
    FIRST_RUN = True

    FILENAME = "clays.db"

    OPTIONS = backend.getClays(FILENAME)

    ROOT = Tk()
    ROOT.title("Delete clay")
    ROOT.geometry("245x150")
    ROOT.resizable(False, False)

    FRAME = Frame(ROOT, padx=5, pady=5)
    FRAME.grid()

    TITLE = Label(FRAME, text="Clay to delete:", font=("Arial", 14))
    TITLE.grid(column=0, row=0, columnspan=3)
    
    OPTIONS = backend.getClays(FILENAME)

    CLAY_CHOICE = StringVar()

    CLAY_OPTIONS = OptionMenu(FRAME, CLAY_CHOICE, *OPTIONS)
    CLAY_OPTIONS.grid(row=1, column=0, sticky=W)

    def deleteButton():
        if CLAY_CHOICE.get() == "":
            pass
        else:
            CLAY_ID = backend.fetchClay(FILENAME, CLAY_CHOICE.get())
            backend.deleteClay(FILENAME, CLAY_ID)
            
            OPTIONS = backend.getClays(FILENAME)

            CLAY_OPTIONS = OptionMenu(FRAME, CLAY_CHOICE, *OPTIONS)
            CLAY_OPTIONS.grid(row=1, column=0, sticky=W)
        
    DELETE_BUTTON = Button(FRAME, text="Delete", command=deleteButton)
    DELETE_BUTTON.grid(row=2, column=0, sticky=W+S)

    def goBack():
        ROOT.destroy()
        mainWindow()

    SEPARATOR_1 = Label(FRAME, text=" ")
    SEPARATOR_1.grid(row=3)

    RETURN_BUTTON = Button(FRAME, text="Return", command=goBack)
    RETURN_BUTTON.grid(row=4, column=0, sticky=W)

    ROOT.mainloop()

if __name__ == "__main__":
    calcClayWindow("Ain't got no main window")
