from tkinter import * # Not generally recommended, but this is the recommended import method for tkinter
from time import sleep

ROOT = Tk()
ROOT.title("Calculator")
ROOT.resizable(False, False)

def AddFunc():
    pass
def clrScreen():
    pass
def clickBtn(number):
    #textBox.delete(0, END)
    textBox.insert(0, number)

textBox = Entry(ROOT, width=35)

btnArray = []
for i in range(10):
    btnArray.append(Button(ROOT, text=f"{i}", padx=40, pady=20, command=lambda: clickBtn(i)))

btnAdd = Button(ROOT, text="+", padx=39, pady=20, command=AddFunc)
btnEql = Button(ROOT, text="=", padx=87, pady=20, command=AddFunc)
btnClr = Button(ROOT, text="CE", padx=84, pady=20, command=clrScreen)

textBox.grid(row=0, column=0, columnspan=3)

for i in range(3):
    btnArray[7 + i].grid(row=1, column=i)
for i in range(3):
    btnArray[4 + i].grid(row=2, column=i)
for i in range(3):
    btnArray[1 + i].grid(row=3, column=i)

btnArray[0].grid(row=4, column=0)

btnAdd.grid(row=5, column=0)
btnClr.grid(row=4, column=1, columnspan=2)
btnEql.grid(row=5, column=1, columnspan=2)

ROOT.mainloop()
