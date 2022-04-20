# tkinter testailuja

from tkinter import Tk, ttk, constants

from .fabric_list_view import FabricListView
from .fabric_info_view import FabricInfoView
from entities.fabric import Fabric

class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_fabric_list_view()
    
    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _handle_add_fabric(self):
        print("add")

    def _handle_search(self):
        print("search")

    def _handle_logout(self):
        print("logged out")

    def _handle_show_fabric(self, *fabric):
        print("show fabric")
        self._show_fabric_info_view(fabric)

    def _handle_info_view_edit_fabric(self):
        print("edit")
    
    def _handle_info_view_delete_fabric(self):
        print("delete")
    
    def _handle_info_view_back(self):
        self._show_fabric_list_view()

    def _show_fabric_list_view(self):
        self._hide_current_view()

        self._current_view = FabricListView(
            self._root,
            self._handle_add_fabric, 
            self._handle_search,
            self._handle_logout,
            self._handle_show_fabric
        )

        self._current_view.pack()
    
    def _show_fabric_info_view(self, fabric:Fabric):
        self._hide_current_view()
        print(fabric)

        self._current_view = FabricInfoView(
            self._root,
            fabric,
            self._handle_info_view_edit_fabric,
            self._handle_info_view_delete_fabric,
            self._handle_info_view_back
        )

        
