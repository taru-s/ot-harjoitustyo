from tkinter import Tk
from ui.gui import GUI

def main():
    window = Tk()
    window.title("Fabric stash")

    app_ui = GUI(window)
    app_ui.start()

    window.mainloop()

main()
