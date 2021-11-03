from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from stocks.charts import PriceChart
from stocks.brokers import BrokerFrame
from stocks.stats import HistoricalDataFrame

class RootWin(Tk):
    # TODO: Not very elegant, adjust this to use a more pythonic approach to storing images in packages
    IMAGES_PATH = "C:\Workspace\Python\Stocks\AlgorithmicTrading\IGNORE\images\\"
    ICON_FILE   = "poivronjaune.ico"
    APP_NAME    = "TSX Screener App"

    def __init__(self, tsx_handle):
        super().__init__()
        # Create a reference to the tsx data passed to this app
        self.tsx = tsx_handle
        # configure the root window
        self.title(self.APP_NAME)
        icon_image = RootWin.IMAGES_PATH+RootWin.ICON_FILE
        self.iconbitmap(icon_image)
        self.geometry('1200x700')
        
        # Define the main menu of the root application (will create a self.main_menu attribute)
        self.__create_main_menu()

        # Main window only has 1 column on which we display all our widgets
        # Main window has 3 rows (header, body, footer) the body (row=1) has the most weight to expand
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.configure(bg="black")
        self.__create_widgets()

    def __create_widgets(self):
        self.header     = HeaderFrame(self, row=0)
        self.body       = EmptyFrame(self, row=1)
        #self.body       = TickerFrame(self, row=1)
        self.status_bar = StatusBarFrame(self, row=2)

    def __create_main_menu(self):
        self.main_menu = Menu(self)
        self.config(menu=self.main_menu)

        file_menu = Menu(self.main_menu, tearoff="off")
        self.main_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New...", command=self.new_command)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.quit)

        self.main_menu.add_cascade(label="Screener", command=self.show_screener_command)
        self.main_menu.add_cascade(label="Broker", command=self.show_broker_command)
        self.main_menu.add_cascade(label="Data", command=self.show_historical_data_command)
        self.main_menu.add_cascade(label="About", command=self.show_about_command)

    def new_command(self):
        # File / New...
        messagebox.showinfo("Debug box", "New command..")

    def show_screener_command(self):
        # Screener
        self.body.grid_forget()
        self.body = ScreenerFrame(self, row=1)
        #messagebox.showinfo("Debug box", "Show Screener command..")        

    def show_broker_command(self):
        # Broker
        self.body.grid_forget()
        self.body = BrokerFrame(self, row=1)

    def show_historical_data_command(self):
        # Data
        self.body.grid_forget()
        self.body = HistoricalDataFrame(self, row=1)


    def show_about_command(self):
        # About
        self.body.grid_forget()
        self.body = AboutFrame(self, row=1)
        


class EmptyFrame(Frame):
    def __init__(self, parent, row=0):
        super().__init__(parent)      
        self.parent = parent
        self.grid(row=row, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        self.configure(bg="Pink")

class AboutFrame(Frame):
    def __init__(self, parent, row=0):
        super().__init__(parent)      
        self.parent = parent
        self.grid(row=row, column=0, sticky='nsew')
        self.rowconfigure(0, weight=1)  
        self.columnconfigure(0, weight=1)
        Label(self, text=f"{RootWin.APP_NAME} is free to use but not to distribute for profit.\n\n\nAll rights reserved Maple Frog Studio, 2021").grid(row=0, column=0)
        self.configure()    


class HeaderFrame(Frame):
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
        self.header_item1 = Label(self, text="Header Item 1",  bg="PeachPuff2")
        self.header_item1.grid(row=0,column=0,sticky="w")        
        self.header_item2 = Label(self, text="Header Item 2",  bg="PeachPuff3")
        self.header_item2.grid(row=0,column=1,sticky="e")
        


class ScreenerFrame(Frame):
    def __init__(self, container, row=0):
        super().__init__(container)
        self.parent = container
        self.grid(row=row, column=0, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.configure(bg="LightSteelBlue1")

        self.__create_widgets()
        self.load_tickers_from_tsx("A")

    def __create_widgets(self):
        self.my_tree = ttk.Treeview(self)
        # Crete a tree lits to display ticker symbol and company information
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
        
        # Double Click handler
        self.my_tree.bind('<Double-1>', self.on_dclick)

        # Display the list on the RootWin
        self.my_tree.grid(row=0,column=0, sticky="nsew")

    def on_dclick(self, event):
        #item = self.my_tree.selection()[0]
        #company_info = self.my_tree.item(item).get('values')
        company_info = self.convert_tree_selectionTo_dict(self.my_tree.selection()[0])
        #print(company_info)
        price_chart = PriceChart(self.parent, company_info)
        # print(f"\n\nPrice Data: {price_chart.prices} ")
        price_chart.plot_something()

    def convert_tree_selectionTo_dict(self, item):
        # item[] => 'ID','Ticker', 'Company Name', 'Exchange', 'Yahoo Symbol', 'Filer'
        info = self.my_tree.item(item).get('values')
        company_info = {
            "ticker"   : info[1],
            "name"     : info[2],
            "exchange" : info[3],
            "yahoo"    : info[4]
        }
        return company_info

    def add_ticker(self, data, highlight):
        # data is dict of the form {"level_0": 3210, "ticker":"ZIK", "name":"some string", "exchange":"tsx","yahoo":"ZIK.TO"}
        # self.ticker_list.insert(END, data)
        ID       = data["level_0"]
        ticker   = data["ticker"]
        name     = data["name"]
        exchange = data["exchange"]
        yahoo    = data["yahoo"]

        # if len(self.my_tree.get_children()) % 2 == 0:
        if highlight:
            self.my_tree.insert(parent='', index='end', iid=ID, values=(ID, ticker, name, exchange, yahoo, ""), tags=('oddrow,'))
        else:
            self.my_tree.insert(parent='', index='end', iid=ID, values=(ID, ticker, name, exchange, yahoo, ""), tags=('evenrow',))
        
    def load_tickers_from_tsx(self, letter):
        # TODO: Make sure Tree View is empty before loading new data to display [ tree.delete(*tree.get_children())) ]
        highlight = True
        companies = self.parent.tsx.get_company_info_for(letter)
        #tsx.get_company_info_for("A")
        for company in companies:
            self.add_ticker(company, highlight)
            highlight = not highlight







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

