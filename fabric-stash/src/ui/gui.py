# tkinter testailuja

from tkinter import messagebox


from .fabric_list_view import FabricListView
from .fabric_info_view import FabricInfoView
from .fabric_edit_view import FabricEditView
from services.fabric_service import FabricService
from entities.fabric import Fabric


class GUI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._service = FabricService()

    def start(self):
        self._show_fabric_list_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _handle_list_view_add_fabric(self):
        self._service.add_fabric("",0,0,0)
        all_ids = self._service.get_all_ids()
        self._show_fabric_edit_view(all_ids[-1])

    def _handle_list_view_search(self):
        print("search")

    def _handle_list_view_logout(self):
        print("logged out")

    def _handle_list_view_show_fabric(self, *fabric_id):
        self._show_fabric_info_view(fabric_id[0])

    def _handle_info_view_edit_fabric(self, *fabric_id):
        self._show_fabric_edit_view(fabric_id[0])

    def _handle_info_view_delete_fabric(self, *fabric_id):
        self._handle_delete_fabric(fabric_id[0])

    def _handle_info_view_back(self):
        self._show_fabric_list_view()

    def _handle_edit_view_save(self, fabric_id, name, width, length, washed_bool):
        washed = 0
        if washed_bool:
            washed = 1
        self._service.edit_fabric(fabric_id, 
                                    name, 
                                    width, 
                                    length, 
                                    washed
                                    )
        print("save")

        self._show_fabric_info_view(fabric_id)

    def _handle_edit_view_delete(self, *fabric_id):
        self._handle_delete_fabric(fabric_id[0])

    def _handle_edit_view_cancel(self, *fabric_id):
        self._show_fabric_info_view(fabric_id[0])

    def _handle_delete_fabric(self, *fabric_id):
        fabric_name = self._service.get_fabric_by_id(fabric_id[0]).name
        delete_confirmation = messagebox.askyesno(
            title="delete fabric",
            message=f"Are you sure you want to delete {fabric_name}?"
            )

        if delete_confirmation:
            self._service.delete_fabric_by_id(fabric_id[0])
            self._show_fabric_list_view()

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

    def _show_fabric_info_view(self, fabric_id):
        self._hide_current_view()

        self._current_view = FabricInfoView(
            self._root,
            fabric_id,
            self._handle_info_view_edit_fabric,
            self._handle_info_view_delete_fabric,
            self._handle_info_view_back
        )

        self._current_view.pack()

    def _show_fabric_edit_view(self, fabric_id):
        self._hide_current_view()

        self._current_view = FabricEditView(
            self._root,
            fabric_id,
            self._handle_edit_view_save,
            self._handle_edit_view_delete,
            self._handle_edit_view_cancel
        )

        self._current_view.pack()
