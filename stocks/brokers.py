from tkinter import *
from tkinter import ttk

class BrokerFrame(Frame):    
    def __init__(self, parent, row=0):
        super().__init__(parent)      
        self.parent = parent
        self.grid(row=row, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        self.configure(bg="Yellow")

        self.__create_widgets()


    def __create_widgets(self):
        Label(self, text=f"Wealth Simple Broker Window").grid(row=0, column=0)
