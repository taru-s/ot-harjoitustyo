from tkinter import Tk
from ui.text_ui import TextUI
from ui.gui import GUI

# ui mode options for debugging
ASK_UI_MODE = False


def main(mode="g"):
    if mode == "t":
        app_ui = TextUI()
        app_ui.start()
    elif mode == "g":
        window = Tk()
        window.title("Fabric stash")

        app_ui = GUI(window)
        app_ui.start()

        window.mainloop()


if ASK_UI_MODE:
    UI_MODE = input("g - gui\nt- text ui\n")
    if UI_MODE not in ('g', 't'):
        UI_MODE = "t"
else:
    UI_MODE = "g"

main(UI_MODE)
