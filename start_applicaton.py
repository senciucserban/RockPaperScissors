import os

from GUI.GUI import GUI
from Controller.Controller import Controller
from Repository.Repository import Repository
from tkinter import *
from tkinter import messagebox

try:
    repo = Repository(os.path.join('Data', 'Data.in'))
    ctrl = Controller(repo)
    root = Tk()
    gui = GUI(root, ctrl)
    root.mainloop()
except IOError as ex:
    messagebox.showerror('Error', ex)
except IndexError as ex:
    messagebox.showerror('Error', ex)
