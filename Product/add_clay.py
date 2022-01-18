from tkinter import *

def addClayWindow():
    ROOT = Tk()

    NAME_LABEL = Label(ROOT, text="Name of clay", font=("Arial", 13), padx=5, pady=5)
    NAME_LABEL.grid(row=0, column=0)

    NAME_ENTRY = Entry(ROOT)
    NAME_ENTRY.grid(row=1, column=0, columnspan=2, sticky=N+S+E+W)

    SHRINK_LABEL = Label(ROOT, text="Name of clay", font=("Arial", 13), padx=5, pady=5)
    SHRINK_LABEL.grid(row=2, column=0)

    SHRINK_ENTRY = Entry(ROOT)
    SHRINK_ENTRY.grid(row=3, column=0, columnspan=2, sticky=N+S+E+W)
    
    ABSORPTION_LABEL = Label(ROOT, text="Name of clay", font=("Arial", 13), padx=5, pady=5)
    ABSORPTION_LABEL.grid(row=4, column=0)

    ABSORPTION_ENTRY = Entry(ROOT)
    ABSORPTION_ENTRY.grid(row=5, column=0, columnspan=2, sticky=N+S+E+W)
    
    ROOT.mainloop()

if __name__ == "__main__":
    addClayWindow()
