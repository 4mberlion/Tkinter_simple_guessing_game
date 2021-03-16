import tkinter as tk
from tkinter import *
import random


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Wybierz przycisk")
        self.master.geometry("300x350")
        self.master.iconphoto(True, PhotoImage(file='icon.png'))
        self.wstaw_przyciski()

    def wstaw_przyciski(self):
        ile_przyciskow = 6
        global przyciski
        przyciski = []
        dobry = random.randint(0, ile_przyciskow - 1)
        for i in range(ile_przyciskow):
            if i == dobry:
                przyciski.append(Button(self.master, text="kliknij mnie", command=self.trafiony))
            else:
                przyciski.append(Button(self.master, text="kliknij mnie", command=self.pudlo))
        for i in przyciski:
            i.pack(fill=BOTH, expand=YES)

    def trafiony(self):
        for i in przyciski:
            i.destroy()
        global etykieta
        etykieta = Label(self.master, text="Trafiłeś dobry przycisk")
        etykieta.pack(fill=BOTH, expand=YES)
        self.master.after(5000, self.restart)

    def pudlo(self):
        for i in przyciski:
            i.destroy()
        global etykieta
        etykieta = Label(self.master, text="Trafiłeś zły przycisk")
        etykieta.pack(fill=BOTH, expand=YES)
        self.master.after(5000, self.restart)

    def restart(self):
        etykieta.destroy()
        self.wstaw_przyciski()


if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
