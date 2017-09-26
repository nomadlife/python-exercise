from tkinter import *

root = Tk()

def key(event):
    print("pressed", "repr:",repr(event.char),"char",event.char)

def callback(event):
    frame.focus_set()
    print("clicked at", event.x, event.y)

frame = Frame(root, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
