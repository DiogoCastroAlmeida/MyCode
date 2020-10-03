from convertion import make_convertion
import tkinter as tk


#class to make the GUI part of the programm
class GuiProgramm():

    def __init__(self, lettertype, lettersize):
        self.lettertype=lettertype
        self.lettersize = lettersize
        self.font=(self.lettertype, self.lettersize)
        self.root=tk.Tk()
        self.root.title("Numbers to Words")
        self.root.geometry("500x175")
        self.welcome_mesage="Welcome to Numbers to Words Programm"


    def show_convertion(self):
        try:
            self.result_label.destroy()
        except:
            pass
        self.result_label=tk.Label(self.root,font=self.font, text=f"{make_convertion(self.entry_box.get())}", justify="center")
        self.result_label.pack()


    def app(self):
        #Initial labels
        self.welcome_label=tk.Label(self.root, text= self.welcome_mesage, font=(self.lettertype, 12, "bold"))
        self.label1=tk.Label(self.root, text="Type bellow the number to be converted", font=self.font)
        self.welcome_label.pack()
        self.label1.pack()
        #Entry Box and Button to get the input
        self.entry_box=tk.Entry(self.root)
        self.convert_button=tk.Button(self.root, text="Convert!", font=self.font, command=self.show_convertion)
        self.entry_box.pack()
        self.convert_button.pack()
        self.root.mainloop()


def run_programm(lettertype, lettersize):
    programm = GuiProgramm(lettertype, lettersize)
    programm.app()

run_programm("Arial", 12)
