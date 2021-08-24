from tkinter import *
from tkinter import ttk

from tsx import TSX

class RootWin(Tk):
    IMAGES_PATH = "C:\Workspace\Python\Stocks\AlgorithmicTrading\IGNORE\images\\"
    ICON_FILE   = "poivronjaune.ico"

    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('TSX Screener App')
        icon_image = RootWin.IMAGES_PATH+RootWin.ICON_FILE
        self.iconbitmap(icon_image)
        self.geometry('1200x700+50+10')
        # Main window only has 1 column on which we display all our widgets
        self.columnconfigure(0, weight=1)
        # Main window has 3 row where row 1 has the weight
        self.rowconfigure(1, weight=1)
        self.configure(bg="light sky blue")

        self.__create_widgets()

    def __create_widgets(self):
        self.menu_bar   = MenuFrame(self, row=0)
        self.tickers    = TickerFrame(self, row=1)
        self.status_bar = StatusBarFrame(self, row=2)


class MenuFrame(Frame):
    # Display on row 0 by default (Top)
    def __init__(self, parent, row=0):
        super().__init__(parent)  
        # Create Header Frame (full width, expanding) on which we will place our widgets
        self.grid(row=row, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        self.configure(bg="PeachPuff")

        # Add widgets at same level as the menu_panel (not on it)
        self.__create_widgets()

    def __create_widgets(self):
        self.menu_item1 = Label(self, text="Item 1",  bg="PeachPuff2")
        self.menu_item1.grid(row=0,column=0,sticky="w")        
        self.menu_item2 = Label(self, text="Item 2",  bg="PeachPuff3")
        self.menu_item2.grid(row=0,column=1,sticky="e")
        

class TickerFrame(Frame):
    def __init__(self, container, row=0):
        super().__init__(container)
        self.grid(row=row, column=0, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.configure(bg="LightSteelBlue1")

        self.__create_widgets()

    def __create_widgets(self):
        self.my_tree = ttk.Treeview(self)
        # Crete a tree lits to displat
        self.my_tree['columns'] = ('ID','Ticker', 'Company Name', 'Exchange', 'Yahoo Symbol', 'Filer')
        self.my_tree.column("#0"          ,           width=0 , stretch=NO)
        self.my_tree.column("ID"          , anchor=W, width=60, stretch=NO)
        self.my_tree.column("Ticker"      , anchor=W, width=75, stretch=NO)
        self.my_tree.column("Company Name", anchor=W, width=150)
        self.my_tree.column("Exchange"    , anchor=W, width=70, stretch=NO)
        self.my_tree.column("Yahoo Symbol", anchor=W, width=75, stretch=NO)
        self.my_tree.column("Filer"       , anchor=E          , stretch=YES)
        # Create headings 
        self.my_tree.heading("#0"          ,text="Label"       , anchor="w")
        self.my_tree.heading("ID"          ,text="ID"          , anchor="w")
        self.my_tree.heading("Ticker"      ,text="Ticker"      , anchor="w")
        self.my_tree.heading("Company Name",text="Company Name", anchor="w")
        self.my_tree.heading("Exchange"    ,text="Exchange"    , anchor="w")
        self.my_tree.heading("Yahoo Symbol",text="Yahoo"       , anchor="w")
        self.my_tree.heading("Filer"       ,text=""            , anchor="e")
        # create striped rows
        self.my_tree.tag_configure('oddrow' , background="white")
        self.my_tree.tag_configure('evenrow', background="lightblue")
        # Doube Click handler
        self.my_tree.bind('<Double-1>', self.on_dclick)

        self.my_tree.grid(row=0,column=0, sticky="nsew")

    def on_dclick(self, event):
        item = self.my_tree.selection()[0]
        list_of_values = self.my_tree.item(item).get('values')
        print(f"Double clicked a line, {list_of_values}")

    def add_ticker(self, data, v):
        # data is dict of the form {"level_0": 3210, "ticker":"ZIK", "name":"some string", "exchange":"tsx","yahoo":"ZIK.TO"}
        #self.ticker_list.insert(END, data)
        ID       = data["level_0"]
        ticker   = data["ticker"]
        name     = data["name"]
        exchange = data["exchange"]
        yahoo    = data["yahoo"]

        # if len(self.my_tree.get_children()) % 2 == 0:
        if v:
            self.my_tree.insert(parent='', index='end', iid=ID, values=(ID, ticker, name, exchange, yahoo, ""), tags=('oddrow,'))
        else:
            self.my_tree.insert(parent='', index='end', iid=ID, values=(ID, ticker, name, exchange, yahoo, ""), tags=('evenrow',))
        
    
    def add_tickers(self, data_list):
        #for ticker in data_list:
        #    self.add_ticker(ticker)
        pass
    
   

class StatusBarFrame(Frame):
    # Display on row 0 by default (Top)
    def __init__(self, parent, row=0):
        super().__init__(parent)  
        # Create Header Frame (full width, expanding) on which we will place our widgets
        self.grid(row=row, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        self.configure(bg="Khaki")

        # Add widgets at same level as the menu_panel (not on it)
        self.__create_widgets()

    def __create_widgets(self):
        self.msg1 = Label(self, text="Status Bar",  bg="Khaki3")
        self.msg1.grid(row=2,column=0,sticky="e")



if __name__ == "__main__":
    root = RootWin()

    tsx = TSX()
    highlight = True
    companies = tsx.get_company_info_for("TSX_Data.sqlite", "A")
    for company in companies:
        root.tickers.add_ticker(company, highlight)
        highlight = not highlight

    print(companies)

    root.mainloop()