from tkinter import *
from tkinter import ttk
import tkinter

# https://stackoverflow.com/questions/28089942/difference-between-fill-and-expand-options-for-tkinter-pack-method/28090362

class HistoricalDataFrame(Frame):    
    def __init__(self, parent, row=0):
        super().__init__(parent)      
        self.parent = parent
        self.tsx_stats = self.parent.tsx.get_tsx_stats()

        self.grid(row=row, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        self.configure(bg="Royal Blue")

        panel_1 = PanedWindow(bd=2, relief=RAISED, bg="red")
        panel_1.grid(row=row, column=0)

        lbl1 = Label(panel_1, text="Panel 1")
        panel_1.add(lbl1)
        lbl1.grid(row=0, column=0)

        panel_2 = PanedWindow(bd=2, relief=RAISED, bg="pink")


class CountsPanelOld(Frame):
    def __init__(self, parent, tsx_stats):
        super().__init__(parent)      
        self.parent = parent
        self.grid(row=0, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        self.configure(bg="Light Blue")

        # Label(self, text=f"Counts Panel").pack(side=tkinter.TOP ,expand=1, fill=tkinter.X)
        # Label(self, text=f'TSX        : {tsx_stats["count_tsx"]}').pack(side=tkinter.LEFT, expand=1, fill=tkinter.X)
        # Label(self, text=f'TSX Venture : {tsx_stats["count_tsxv"]}').pack(side=tkinter.LEFT, expand=1, fill=tkinter.X)
        # Label(self, text=f"Counts Panel").grid(self, row=0, column=0, columnspan=3)

        # Label(self, text=f'TSX').grid(self, row=1, column=0)
        # Label(self, text=f':').grid(self, row=1, column=1)
        # Label(self, text=f'{tsx_stats["count_tsx"]}').grid(self, row=1, column=2)

        # Label(self, text=f'TSX Venture').grid(self, row=2, column=0)
        # Label(self, text=f':').grid(self, row=2, column=1)
        # Label(self, text=f'{tsx_stats["count_tsxv"]}').grid(self, row=2, column=2)
