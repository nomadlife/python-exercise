# menu

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def closeApp():
    root.quit()

def showAbout(event=None):
    messagebox.showwarning("About",
                           "This Awesome Program was Made in 2017")

root =Tk()

# Create the
theMenu = Menu(root)

# ----------File Menu -------------
# Create a pull down menu that can't be removed
fileMenu = Menu(theMenu, tearoff=0)
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save")
fileMenu.add_separator()
fileMenu.add_command(label="Quit",command=closeApp())
theMenu.add_cascade(label="File", menu = fileMenu)

# ------------FONT MENU---------------
fontVar = StringVar()
fontVar.set("Times")

def change_font(event=None):
    print("Font Picked :", fontVar.get())
fontMenu = Menu(theMenu, tearoff=0)

fontMenu.add_radiobutton(label="Times", variable=fontVar, command=change_font)
fontMenu.add_radiobutton(label="Courier", variable=fontVar, command=change_font)
fontMenu.add_radiobutton(label="Ariel", variable=fontVar, command=change_font)

# -------- VIEW MENU ------
viewMenu = Menu(theMenu, tearoff=0)
lineNumberVar = IntVar()
lineNumberVar.set(1)

viewMenu.add_checkbutton(label="Line Numbers", variable=lineNumberVar)
viewMenu.add_cascade(label="Fonts", menu=fontMenu)
theMenu.add_cascade(label="View", menu=viewMenu)

# ------HELP MENU---------
helpMenu = Menu(theMenu, tearoff=0)
helpMenu.add_command(label="About", accelerator="command-H", command=showAbout)
theMenu.add_cascade(label="Help", menu=helpMenu)

root.bind('<Command-A>', showAbout)
root.bind('<Command-a>', showAbout)

root.config(menu=theMenu)

root.mainloop()
