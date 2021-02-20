from tkinter import *
class Utilities():
    @staticmethod
    def remove_characters_from_string(string, characters_to_remove):
        for character in characters_to_remove:
            string = string.replace(character, "")
        return string



class Calculator():

    maths_operations_and_symbols = ["+", "-", "/", "*", "^", ",", "(", ")", "[", "]"]
    def __init__(self, operation):
        self.operation= operation

#list with some exceptions that happen in python
    exception=[["^"],["**"]]

    def is_valid (self):
        try:
            float(Utilities.remove_characters_from_string(self.operation, self.maths_operations_and_symbols))
        except:
            return False
        else:
            return True



    def check_for_special(self):
        for character in range(len(self.exception[0])):
            self.operation = self.operation.replace(self.exception[0][character], self.exception[1][character])


    def make_operation(self):
        if self.is_valid() == False:
            return "Invalid Input"
        else:
            return eval(self.operation)




def run(operation):
    calculator = Calculator(operation)
    calculator.check_for_special()
    calculator.operation
    return calculator.make_operation()


class Gui():

    def show_result(self, operation):
        try:
            self.result_label.destroy()
        except:
            pass
        try:
            self.result_label=Label(self.root, text=f"{run(operation=operation)}")
        except:
            pass
        self.result_label.pack()


    def make_gui(self):
        self.root=Tk()
        self.root.title = "Calculator"
        self.initial_label=Label(self.root, text="Welcome! Type the operation bellow.")
        self.operation_entry = Entry(self.root)
        self.operation_button = Button(self.root, text="Calculate!", command=lambda: self.show_result(self.operation_entry.get()))
        self.initial_label.pack()
        self.operation_entry.pack()
        self.operation_button.pack()
        self.root.mainloop()


a=Gui()
a.make_gui()
