import tkinter
from tkinter import *
from tkinter import ttk, filedialog

def update(): #Update weather and news save
    print("update")
def openSettings(): #Open a settings menu
    print("settings")
def newsWin():
    print("news")
def weatherWin():
    print("weather")

root = tkinter.Tk()
root.title("Update")

menubar = Menu(root)
casc = Menu(root, tearoff=False)
root.config(menu=menubar)

casc.add_command(label="Update",command=update)
casc.add_command(label="Settings",command=openSettings)

menubar.add_cascade(label="File", menu=casc)
menubar.add_command(label="News", command=newsWin)
menubar.add_command(label="Weather", command=weatherWin)

root.mainloop()