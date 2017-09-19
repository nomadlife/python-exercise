from tkinter import *
from tkinter import ttk
class Calculator:
    clac_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):
        entry_val = self.number_entry.get()
        entry_val += value
        self.number_entry.delete(0,"end")
        self.number_entry.insert(0,entryVal)

    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self,value):
        if self.isfloat(str(self.number_entry.get())):
            self.add_trigger = False
            self.sub_trigger = False
            self.mult_trigger = False
            self.div_trigger = False

            self.calc_value = float(self.entry_value.get())

            if value == "/":
                print("/ pressed")
                self.div_trigger = True
            elif value == "*":
                print("* pressed")
                self.mult_trigger = True
            elif value == "+":
                print("+ pressed")
                self.add_trigger = True
            else :
                print("- pressed")
                self.sub_trigger = True
            self.number_entry.delete(0,"end")
            
