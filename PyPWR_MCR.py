import time
import math
import sys
from colorama import Fore
from tkinter import *
import tkinter as tk
from tkinter import ttk
panel_x = -320
show_panel_x = 0
MP = False

def Reactor_window():
    canvas1.destroy()
    progressbar = ttk.Progressbar(master, orient=HORIZONTAL, length=200, mode='indeterminate', )
    progressbar.place(x = 600, y = 700)
    progressbar.start


master = Tk()   
master.geometry('1800x1600')
master.title("Multiple Control Rod Stationary Low Power NPPS")
bg = tk.PhotoImage(file = "TMI__.png")
# Create Canvas 
canvas1 = Canvas(master, width = 1800, 
                 height = 1600)

master.attributes('-fullscreen',True)
canvas1.pack(fill = "both", expand = True) 

# Display image 
canvas1.create_image(1000, 500, image = bg)

# Create Buttons 
button3 = Button( master, text = "Start", command = Reactor_window) 
button1 = Button( master, text = "Exit", command = master.destroy) 
  
# Create Lables
lable1 = Label(master, text = 'Welcome', font = ("AppleGothic", 30))
lable2 = Label(master, text = 'Sydney Nuclear Services', font = ("Snell Roundhand", 15))

# Display Lables
lable1_canvas = canvas1.create_window(35, 10,
                             anchor = "nw",
                             window = lable1)

lable2_canvas = canvas1.create_window(0, 1025,
                             anchor = "nw",
                             window = lable2)

# Display Buttons 
button1_canvas = canvas1.create_window( 70, 75,  
                                       anchor = "nw", 
                                       window = button1)  
  
button3_canvas = canvas1.create_window( 67, 110, anchor = "nw", 
                                       window = button3) 



master.mainloop() 