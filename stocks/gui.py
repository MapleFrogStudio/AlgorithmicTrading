import os
import tkinter as tk

from PIL import Image, ImageTk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


class GUI_env():
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__name__))
        self.data = "\DATA"

    @property
    def databases(self):
        db_path = self.path + self.data
        files = os.listdir(db_path)
        databases = []
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension == ".sqlite":
                databases.append(filename)
        if len(databases) < 1:
            databases = None
        
        return databases

class GUI_Plot():
    def __init__(window):
        fig = Figure(figsize = (5,5), dpi= 100)
        y = [i**2 for i in range(101)]
        plot1 = fig.add_subplot(111)

        plot1.plot(y)
        canvas = FigureCanvasTkAgg(fig, master = window)  
        canvas.draw()

        canvas.get_tk_widget().pack()
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        canvas.get_tk_widget().pack()


class GUI():
    FONT = 'Raleway'

    BTN_BG_COLOR = '#20bebe'
    BTN_FG_COLOR = 'white'
    BTN_HEIGHT   = 1
    BTN_WIDTH    = 10

    def __init__(self):
        print(f"Gui app loading...")
        self.env = GUI_env()

        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=1500, height=800)
        self.canvas.grid(columnspan=8, rowspan=6)

        self.display_logo('logo.png',1,0)
        self.display_instructions("Select a PDF file on your computer to extract all its text")
        self.display_button( 'Plot', 1, 2)

        
        self.show_env()

        self.root.mainloop()
    
    # def __init__(self) -> None:
    #     # Main tkinter window
    #     self.window = Tk()

    #     # Setting the tilte
    #     self.window.title('Plotting in TKinter')

    #     self.window.geometry("1100x500")

    #     # Button that will display the plot
    #     width, height = 10, 2
    #     plot_button = Button(
    #         master = self.window,
    #         height = height,
    #         width  = width,
    #         text   = f"Plot {width, height} "
    #     )

    #     # Place the button in the window
    #     plot_button.pack()

    #     # Run the GUI loop
    #     self.window.mainloop()

    def display_logo(self, logofile, col, row):
        # Load logo as a Pillow image
        logo = Image.open(logofile)
        logo = ImageTk.PhotoImage(logo)
        self.logo_label = tk.Label(image=logo)
        self.logo_label.image = logo
        self.logo_label.grid(column=col, row=row)

    def display_instructions(self, msg):
        self.instructions = tk.Label(self.root, text=msg, font=GUI.FONT)
        self.instructions.grid(columnspan=3, column=0, row=1)
 
    def display_button(self, text, col, row):
        browse_txt = tk.StringVar()
        browse_btn = tk.Button(self.root, textvariable=browse_txt, 
                                font=GUI.FONT, 
                                bg    = GUI.BTN_BG_COLOR,
                                fg    = GUI.BTN_FG_COLOR,
                                height= GUI.BTN_HEIGHT,
                                width = GUI.BTN_WIDTH,
                                command=self.Plot
                                )
        browse_txt.set(text)
        browse_btn.grid(column=col, row=row)

    def Plot(self):
        print(f"Plot funct  : No used")
        pass
    #     fig = Figure(figsize = (5,5), dpi= 100)
    #     y = [i**2 for i in range(101)]
    #     plot1 = fig.add_subplot(111)

    #     plot1.plot(y)
    #     canvas = FigureCanvasTkAgg(fig, master = self.root)  
    #     canvas.draw()

    #     canvas.get_tk_widget().pack()
    #     toolbar = NavigationToolbar2Tk(canvas, self.root)
    #     toolbar.update()
    #     canvas.get_tk_widget().pack()


    # DEBUG STUFF
    def show_env(self):
        print(f"os path     : {self.env.path} ")
        print(f"data folder : { self.env.path}{self.env.data } ")
        print(f"files       : {self.env.databases}")
        
