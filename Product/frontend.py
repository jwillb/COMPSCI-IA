from tkinter import * # Not generally recommended, but this is the recommended import method for tkinter
from tkinter import ttk

ROOT = Tk()
ROOT.title("Pottery Calculator")
ROOT.geometry("360x640")

MAIN_FRAME = ttk.Frame(ROOT, padding="10") # Create window frame
MAIN_FRAME.grid()

ROOT.mainloop()
