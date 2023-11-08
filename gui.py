import tkinter
from datetime import datetime
from tkinter import *
from tkinter import ttk, filedialog
import newsapi, weather

# Useful functions
def update(): #Update weather and news save
    weather.updateData
    curweather = weather.getWeather
    now = datetime.now()
    now = now.strftime("%d/%m/%/y, %H/%M")
    return now, curweather # returned as temp list, rain list

root = tkinter.Tk()
root.title("Update")

# Tabs setup
tabs = ttk.Notebook(root)
tabs.pack(pady=10, expand=True, anchor='nw')

mainmenuFrame = ttk.Frame(tabs)
weatherFrame = ttk.Frame(tabs)
newsFrame = ttk.Frame(tabs)

mainmenuFrame.pack(fill='both', expand=True)
weatherFrame.pack(fill='both', expand=True)
newsFrame.pack(fill='both', expand=True)

tabs.add(mainmenuFrame, text= "Main Menu")
tabs.add(weatherFrame, text="Weather")
tabs.add(newsFrame, text="News")

#Main menu
menuInfo = Label(mainmenuFrame, text="Info",justify='left')
menuSettings = Label(mainmenuFrame, text="Settings",justify='left')
menuInfo.grid(row=0)
menuSettings.grid(row=0,column=1)

info = Label(mainmenuFrame,text="Created by DevL",justify='left')
info1 = Label(mainmenuFrame,text="Last updated 11/6/23",justify='left')

info.grid(row=1,column=0)
info1.grid(row=2,column=0)

refreshLabel = Label(mainmenuFrame, text="Refresh All")
zipcodeLabel = Label(mainmenuFrame,text="Zipcode")

refresh = Button(mainmenuFrame, text="Refresh", command=update,width=5,height=1)
zipcode = Text(mainmenuFrame,width=5,height=1)

refreshLabel.grid(row=1,column=1)
refresh.grid(row=1,column=2)
zipcodeLabel.grid(row=2,column=1)
zipcode.grid(row=2,column=2)

#Weather tab

root.mainloop()