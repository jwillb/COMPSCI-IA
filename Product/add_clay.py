from tkinter import *
from tkinter import ttk

def addClayWindow():
    ROOT = Tk()
    ROOT.title("Add a new clay type")
    ROOT.geometry("240x250")
    ROOT.resizable(False, False)

    FRAME = Frame(ROOT, padx=5, pady=2)
    #FRAME.grid(row=0, column=0)

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

    SEPARATOR = ttk.Separator(FRAME)
    SEPARATOR.grid(column=0, row=6, columnspan=3)

    ADD_BUTTON = Button(FRAME, text="Add!", width=16)
    ADD_BUTTON.grid(row=7, column=0, sticky=E)

    ROOT.mainloop()

if __name__ == "__main__":
    addClayWindow()
