from time import time, sleep
from tkinter import *

def empty_textbox():
    textbox.insert(END, 'This is a test')
    sleep(5)
    textbox.delete("1.0", END)

root = Tk()

frame = Frame(root, width=300, height=100)
textbox = Text(frame)

frame.pack_propagate(0)
frame.pack()
textbox.pack()

empty_textbox()

root.mainloop()