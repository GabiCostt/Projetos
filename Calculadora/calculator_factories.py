import tkinter as tk
from typing import List

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title('Calculadora')
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)
    return root

def make_label(root) -> tk.Label:
    label = tk.Label(text='Sem conta ainda',
                    anchor='e',
                    justify='right',
                    background='#fff')
    label.grid(row=0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry()
    display.grid(row=1, column=0, columnspan=5, sticky='news', pady=(0, 10))
    display.config(font='Helvetica',
                   justify='right',
                   background='#fff',
                   bd=1, relief='flat',
                   highlightthickness=1,
                   highlightcolor='#ccc')
    display.bind('<Control-a>', _display_control_a)
    return display

def _display_control_a(event):
    event.widget.select_range(0, 'end')
    event.widget.icursor('end')
    return 'break'

def make_button(root) -> List[List[tk.Button]]:
    buttons_texts = List[List[str]] = [
        ['7', '8', '9', '+', 'C']
        ['4', '5', '6', '-', '/']
        ['1', '2', '3', '*', '^']
        ['0', '.', '(', ')', '=']
    ]
    buttons = List[List[tk.Button]] = []

    #for row_index, row_value in enumerate(buttons_texts, start=2):
        
