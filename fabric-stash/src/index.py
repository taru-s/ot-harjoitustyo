from ui.text_ui import TextUI
from ui.gui import GUI
from tkinter import Tk


def main(mode="g"):
    if mode=="t":
        ui = TextUI()
        ui.start()
    elif mode=="g":
        window = Tk()
        window.title("Fabric stash")

        ui = GUI(window)
        ui.start()

        window.mainloop()

input_mode = input("g - gui\nt- text ui\n")
if input_mode not in ('g', 't'):
    input_mode="t"
main(input_mode)