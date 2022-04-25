# tkinter testailuja

from tkinter import Tk, ttk, constants

from .fabric_list_view import FabricListView
from .fabric_info_view import FabricInfoView
from .fabric_edit_view import FabricEditView
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

    def _handle_list_view_add_fabric(self):
        print("add")

    def _handle_list_view_search(self):
        print("search")

    def _handle_list_view_logout(self):
        print("logged out")

    def _handle_list_view_show_fabric(self, *fabric):
        self._show_fabric_info_view(fabric[0])

    def _handle_info_view_edit_fabric(self, *fabric):
        self._show_fabric_edit_view(fabric[0])

    def _handle_info_view_delete_fabric(self):
        print("delete")

    def _handle_info_view_back(self):
        self._show_fabric_list_view()

    def _handle_edit_view_save(self):
        print("save")

    def _handle_edit_view_delete(self):
        print("delete")

    def _handle_edit_view_cancel(self, *fabric):
        self._show_fabric_info_view(fabric[0])

    def _show_fabric_list_view(self):
        self._hide_current_view()

        self._current_view = FabricListView(
            self._root,
            self._handle_list_view_add_fabric,
            self._handle_list_view_search,
            self._handle_list_view_logout,
            self._handle_list_view_show_fabric
        )

        self._current_view.pack()

    def _show_fabric_info_view(self, fabric=Fabric("no fabric", 0, 0, False)):
        self._hide_current_view()

        self._current_view = FabricInfoView(
            self._root,
            fabric,
            self._handle_info_view_edit_fabric,
            self._handle_info_view_delete_fabric,
            self._handle_info_view_back
        )

        self._current_view.pack()

    def _show_fabric_edit_view(self, fabric=Fabric("no fabric", 0, 0, False)):
        self._hide_current_view()

        self._current_view = FabricEditView(
            self._root,
            fabric,
            self._handle_edit_view_save,
            self._handle_edit_view_delete,
            self._handle_edit_view_cancel
        )

        self._current_view.pack()
