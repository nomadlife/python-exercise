from tkinter import *
from tkinter import ttk

class Calculator:
    calc_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False
    answer_trigger = False
    operators = '+-*/'
    numbers = '1234567890'

    def key(self,value):
        print(value,"repr:",repr(value.char),"char:",value.char)

        if repr(value.char) == "''":
            return

        elif value.char in self.operators:
            self.math_button_press(value.char)

        elif value.char in self.numbers:
            self.button_press(value.char)

        elif repr(value.char) == "'\\r'":
            self.equal_button_press()

        elif repr(value.char) == "'\\x1b'":
            self.button_press('AC')

        elif repr(value.char) == "'\\x08'":
            if not self.answer_trigger == True:
                self.number_entry_delete_backspace()


    def history_entry_insert(self, value):
        self.history_entry.configure(state='normal')
        self.history_entry.insert(0,value)
        self.history_entry.configure(state='disabled')

    def history_entry_delete(self):
        self.history_entry.configure(state='normal')
        self.history_entry.delete(0,"end")
        self.history_entry.configure(state='disabled')

    def number_entry_insert(self, value):
        self.number_entry.configure(state='normal')
        self.number_entry.insert(0,value)
        self.number_entry.configure(state='disabled')

    def number_entry_delete(self):
        self.number_entry.configure(state='normal')
        self.number_entry.delete(0,"end")
        self.number_entry.configure(state='disabled')

    def number_entry_delete_backspace(self):
        self.number_entry.configure(state='normal')
        txt = self.entry_value.get()[:-1]
        self.number_entry.delete(0,"end")
        self.number_entry.insert(txt)
        self.number_entry.configure(state='disabled')

    def symbol_entry_insert(self, value):
        self.symbol_entry.configure(state='normal')
        self.symbol_entry.insert(0,value)
        self.symbol_entry.configure(state='disabled')

    def symbol_entry_delete(self):
        self.symbol_entry.configure(state='normal')
        self.symbol_entry.delete(0,"end")
        self.symbol_entry.configure(state='disabled')

    def math_trigger_false(self):
        self.add_trigger = False
        self.sub_trigger = False
        self.mult_trigger = False
        self.div_trigger = False

    def is_triggered(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            return True
        else:
            return False

    def button_press(self, value):
        if value == 'AC':
            self.number_entry_delete()
            self.symbol_entry_delete()
            self.history_entry_delete()
            self.calc_value = 0.0
            self.math_trigger_false()
        else:
            if self.answer_trigger == True:
                self.history_entry_delete()
                self.number_entry_delete()
                self.answer_trigger = False
            entry_val = self.number_entry.get()
            entry_val += value
            self.number_entry_delete()
            self.number_entry_insert(entry_val)

    def isfloat(self, str_val):
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    def math_button_press(self,value):
        if self.isfloat(str(self.number_entry.get())):
            if self.is_triggered():
                self.equal_button_press()
            self.math_trigger_false()

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

            if self.answer_trigger == True:
                self.history_entry_delete()
                self.answer_trigger = False

            self.history_entry_insert(str(self.calc_value))
            self.number_entry_delete()
            self.symbol_entry_insert(value)

        elif self.is_triggered():
            self.math_trigger_false()
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
            self.symbol_entry_delete()
            self.symbol_entry_insert(value)

    def equal_button_press(self):
        if self.is_triggered():
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger :
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())
            self.math_trigger_false()

            print(self.calc_value, " ", float(self.entry_value.get()), " ", solution)

            log_value = self.history_value.get()+self.symbol_value.get()+self.entry_value.get()
            self.history_entry_delete()
            self.history_entry_insert(log_value)

            self.number_entry_delete()
            self.number_entry_insert(solution)

            self.symbol_entry_delete()

            self.answer_trigger = True


    def __init__(self,root):
        self.entry_value = StringVar(root, value="")
        self.symbol_value = StringVar(root, value="")
        self.history_value = StringVar(root, value="")

        root.title("Calculator")
        root.geometry("630x250")
        root.resizable(width=False, height=False)

        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry",font="Serif 18", padding=10)

        self.history_entry = ttk.Entry(root, textvariable=self.history_value,
                    width=23,state='disabled',font="Serif 16")
        self.history_entry.grid(row=0,columnspan=4, stick=W)

        self.number_entry = ttk.Entry(root, textvariable=self.entry_value,
                    width=23,state='disabled',font="Serif 16")
        self.number_entry.grid(row=0,columnspan=4, stick=E)

        self.symbol_entry = ttk.Entry(root, textvariable=self.symbol_value,
                    width=2,state='disabled',font=("Serif",16))
        self.symbol_entry.grid(row=0,columnspan=4)


        self.button7=ttk.Button(root, text="7", command=lambda:
        self.button_press('7')).grid(row=1,column=0)

        self.button8=ttk.Button(root, text="8", command=lambda:
        self.button_press('8')).grid(row=1,column=1)

        self.button9=ttk.Button(root, text="9", command=lambda:
        self.button_press('9')).grid(row=1,column=2)

        self.button_div=ttk.Button(root, text="/", command=lambda:
        self.math_button_press('/')).grid(row=1,column=3)


        self.button4=ttk.Button(root, text="4", command=lambda:
        self.button_press('4')).grid(row=2,column=0)

        self.button5=ttk.Button(root, text="5", command=lambda:
        self.button_press('5')).grid(row=2,column=1)

        self.button6=ttk.Button(root, text="6", command=lambda:
        self.button_press('6')).grid(row=2,column=2)

        self.button_mult=ttk.Button(root, text="*", command=lambda:
        self.math_button_press('*')).grid(row=2,column=3)


        self.button1=ttk.Button(root, text="1", command=lambda:
        self.button_press('1')).grid(row=3,column=0)

        self.button2=ttk.Button(root, text="2", command=lambda:
        self.button_press('2')).grid(row=3,column=1)

        self.button3=ttk.Button(root, text="3", command=lambda:
        self.button_press('3')).grid(row=3,column=2)

        self.button_add=ttk.Button(root, text="+", command=lambda:
        self.math_button_press('+')).grid(row=3,column=3)


        self.button_clear=ttk.Button(root, text="AC", command=lambda:
        self.button_press('AC')).grid(row=4,column=0)

        self.button0=ttk.Button(root, text="0", command=lambda:
        self.button_press('0')).grid(row=4,column=1)

        self.button_equal=ttk.Button(root, text="=", command=lambda:
        self.equal_button_press()).grid(row=4,column=2)

        self.button_sub=ttk.Button(root, text="-", command=lambda:
        self.math_button_press('-')).grid(row=4,column=3)

        root.bind('<Key>',self.key)

root = Tk()

calc = Calculator(root)

root.mainloop()
