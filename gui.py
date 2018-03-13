#!/usr/bin/env python
import tkinter as tk
from units import unit, predefined  # requires pip package; TODO: bundle

class App:
    def __init__(self, root):
        top_frame = tk.Frame(root)
        top_frame.pack()
        
        self.number = tk.DoubleVar()  # floating point
        self.number_button = tk.Entry(top_frame,
                                      textvariable=self.number)
        self.number_button.pack(side='left')

        self.from_units = tk.StringVar()
        self.from_units.set("meters")

        self.from_units_button = tk.Entry(top_frame,
                                          textvariable=self.from_units)
        self.from_units_button.pack(side='right')


        self.convert_button = tk.Button(root, text="Convert",
                                        command=self.convert)
        self.convert_button.pack(side='bottom')


        middle_frame = tk.Frame(root)
        middle_frame.pack(side='bottom')
        
        self.to_units = tk.StringVar()
        self.to_units.set("ft")
        self.to_units_button = tk.Entry(middle_frame,
                                        textvariable=self.to_units)
        self.to_units_button.pack(side='right')
        
        self.result = tk.DoubleVar()
        self.result_button = tk.Label(middle_frame,
                                      textvariable=self.result)
        self.result_button.pack(side='left')
        
    def convert(self):
        pass  # TODO
                
root = tk.Tk()
root.title("Units converter")
app = App(root)

root.mainloop()

try:
    root.destroy()
except tk.TclError:  # already destroyed
    pass
