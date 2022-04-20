# tkinter testailuja

from tkinter import Tk, ttk, constants
from .fabric_list_view import FabricListView

class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_fabric_list_view()

    def _handle_add_fabric(self):
        print("add")

    def _handle_search(self):
        print("search")

    def _handle_logout(self):
        print("logged out")

    def _show_fabric_list_view(self):
        self._current_view = FabricListView(
            self._root, 
            self._handle_add_fabric, 
            self._handle_search,
            self._handle_logout
        )

        self._current_view.pack()
