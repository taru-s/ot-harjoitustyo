from ui.text_ui import TextUI
from ui.gui import GUI
from tkinter import Tk


def main(mode="gui"):
    if mode=="text":
        ui = TextUI()
        ui.start()
    elif mode=="gui":
        window = Tk()
        window.title("Fabric stash")

        ui = GUI(window)
        ui.start()

        window.mainloop()

main("text")