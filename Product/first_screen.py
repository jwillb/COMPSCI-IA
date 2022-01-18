from tkinter import *

ROOT = Tk()
ROOT.resizable(False, False)

ADD = IntVar()
CALC = IntVar()

def flipCalc():
    if ADD.get():
        CALC.set(0)
    else:
        CALC.set(1)

def flipAdd():
    if CALC.get():
        ADD.set(0)
    else:
        ADD.set(1)

TITLE = Label(ROOT, text="Select mode:", padx=100, pady=20, font=("Arial", 15))
TITLE.grid(row=0, column=0, columnspan=3)

CALC_CLAY = Checkbutton(ROOT, padx=10, pady=10, variable=CALC, onvalue=1, offvalue=0, command=flipAdd)
CALC_CLAY.grid(row=1, column=0)

CALC_LABEL = Label(ROOT, text="Calculate shrinkage of a pot", padx=5)
CALC_LABEL.grid(row=1, column=1, columnspan=2, sticky=W)

ADD_CLAY = Checkbutton(ROOT, padx=10, pady=10, variable=ADD, onvalue=1, offvalue=0, command=flipCalc)
ADD_CLAY.grid(row=2, column=0)

ADD_LABEL = Label(ROOT, text="Add a new clay type", padx=5)
ADD_LABEL.grid(row=2, column=1, columnspan=1, sticky=W)

CONFIRM_BTN = Button(ROOT, text="Ok", width=16)
CONFIRM_BTN.grid(row=3, column=1, sticky=W)

ROOT.mainloop()
