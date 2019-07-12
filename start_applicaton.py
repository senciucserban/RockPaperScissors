#!/usr/bin/env python
import os
from tkinter import *
from tkinter import messagebox

from GUI.GUI import GUI
from controller.controller import Controller
from repository.repository import Repository

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
