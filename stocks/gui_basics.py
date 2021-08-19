from tkinter import *

root = Tk()

# Widgets are the basic component for tkinter to display stuff
# Create the widget, the position it on the screen

# Create a label widget and pack() it in the root window, later we will position it
myLabel = Label(root, text="Hello World!")
myLabel.pack()










# Run this module if called directly and not imported
if __name__ == '__main__':
    print(f"---- Start prpgram ----")
    print(f"---- Lauching TKinter GUI Loop ----")
    root.mainloop()
    print(f"---- End of prpgram ----")