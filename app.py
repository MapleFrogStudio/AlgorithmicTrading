from datetime import datetime
import time
import sys
from typing import Text

from dotenv import load_dotenv
load_dotenv()

# https://pysimplegui.readthedocs.io/en/latest/
import PySimpleGUI as sg

# Maple Frog Studio Packages (TODO: Implement as a real package)
import stocks
import dmaco


WIN_W = 90
WIN_H = 25
START_UP = True
filename = None

# 2 - Layout Defintio (of the main window)
file_new    = "New.........(ctrl+n)"
file_open   = "Open........(ctrl+o)"
file_save   = "Save........(ctrl+s)"
menu_layout = [ ['File', [file_new, file_open, file_save, 'Save as', '---', 'Exit']],
                ['Tools', ['Word Count']],
                ['Help', ['About']]
              ]

layout = [  [sg.Menu(menu_layout)],
            [sg.Text('> New file <', font=('Consolas', 10), size=(WIN_W, 1), key='__INFO__' )],
            [sg.Multiline(font=('Consolas', 10), size=(WIN_W, WIN_H), key='__BODY__') ]]

sg.theme('DarkAmber') 

# 3 - Create the window
window = sg.Window('Notepad', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True, finalize=True)

# 4 - Event loop (to display and adjust the windows layout sections with new information)
window.maximize()
window['__BODY__'].expand(expand_x=True, expand_y=True)
while True:
    event, values = window.read(timeout=1)
    
    if event in (None, 'Exit'):
        break

# 5 - Close the window
window.close()