import pyautogui
import tkinter as tk
from tkinter import filedialog
from numpy import *

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()
def screenshot():
    myScreenshot = pyautogui.screenshot()
    file_path = filedialog.asksaveasfilename(defaultextension='.png')
    myScreenshot.save(file_path)
mybutton = tk.Button(text = "screenshot", command = screenshot, bg = "white", fg = "black", font = 10)


canvas1.create_window(150, 150, window = mybutton)


root.mainloop()