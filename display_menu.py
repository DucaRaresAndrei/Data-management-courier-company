from tkinter import *
import pyodbc
import pyodbc
from PIL import ImageTk
from tkinter import  messagebox
from second_window import *

class DisplayMenu(SecondWindow):

    def display_couriers(self):
        self.insert_frame = Canvas(self.window, bg="white", height=650, width=500)
        self.insert_frame.place(x=250, y=70)