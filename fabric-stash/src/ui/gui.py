# tkinter testailuja

from tkinter import messagebox


from .fabric_list_view import FabricListView
from .fabric_info_view import FabricInfoView
from .fabric_edit_view import FabricEditView
from .fabric_search_view import FabricSearchView
from services.fabric_service import FabricService


class GUI:
    """Class for managing the Graphical User Interface and handling user commands
    """
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._service = FabricService()

    def start(self):
        self._show_fabric_list_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()


    # general handlers

    def _add_fabric(self):
        """Adds a 'dummy fabric' to the database, and shows it in edit view.
        """
        self._service.add_fabric("",0,0,0)
        all_ids = self._service.get_all_ids()
        self._show_fabric_edit_view(all_ids[-1], True)
    

    def _delete_fabric(self, *fabric_id):
        """Asks for confirmation for deleting the given fabric.
        If user confirms, deletes the fabric and shows the list view.
        If user declines, doesn't do anything.
        """
        fabric_name = self._service.get_fabric_by_id(fabric_id[0]).name
        delete_confirmation = messagebox.askyesno(
            title="delete fabric",
            message=f"Are you sure you want to delete {fabric_name}?"
            )

        if delete_confirmation:
            self._service.delete_fabric_by_id(fabric_id[0])
            self._show_fabric_list_view()


    # list view handlers

    def _handle_list_view_add_fabric(self):
        self._add_fabric()

    def _handle_list_view_search(self):
        self._show_fabric_search_view()

    def _handle_list_view_logout(self):
        print("logged out")

    def _handle_list_view_show_fabric(self, *fabric_id):
        self._show_fabric_info_view(fabric_id[0])


    # info view handlers

    def _handle_info_view_edit_fabric(self, *fabric_id):
        self._show_fabric_edit_view(fabric_id[0], False)

    def _handle_info_view_delete_fabric(self, *fabric_id):
        self._delete_fabric(fabric_id[0])

    def _handle_info_view_back(self):
        #TODO change to show the list or search view depending on where the user came from
        self._show_fabric_list_view()

    
    # edit view handlers

    def _handle_edit_view_save(self, fabric_id, name, width, length, washed):
        # washed = 0
        # if washed_bool:
        #     washed = 1
        self._service.edit_fabric(fabric_id,
                                  name,
                                  width,
                                  length,
                                  washed
                                  )

        self._show_fabric_info_view(fabric_id)

    def _handle_edit_view_delete(self, *fabric_id):
        self._delete_fabric(fabric_id[0])

    def _handle_edit_view_cancel(self, from_add_new, *fabric_id):
        if from_add_new:
            self._service.delete_fabric_by_id(fabric_id[0])
            self._show_fabric_list_view()
        else:
            self._show_fabric_info_view(fabric_id[0])

    
    # search view handlers

    def _handle_search_view_add(self):
        self._add_fabric()

    def _handle_search_view_list(self):
        self._show_fabric_list_view()

    def _handle_search_view_show_fabric(self, *fabric_id):
        self._show_fabric_info_view(fabric_id[0])


    # 'show view' methods

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

    def _show_fabric_edit_view(self, fabric_id: int, from_add_new: bool):
        """Shows fabric in edit view.

        Args:
            fabric_id (int): id of the fabric to be shown
            from_add_new (bool): A boolean value for whether the user is coming to the edit view
                    from adding a new fabric, or not. Used for deciding what to do when cancelling
                    out of the edit view.
        """

        self._hide_current_view()

        self._current_view = FabricEditView(
            self._root,
            fabric_id,
            from_add_new,
            self._handle_edit_view_save,
            self._handle_edit_view_delete,
            self._handle_edit_view_cancel
        )

        self._current_view.pack()

    def _show_fabric_search_view(self):
        self._hide_current_view()

        self._current_view = FabricSearchView(
            self._root,
            self._handle_search_view_add,
            self._handle_search_view_list,
            self._handle_search_view_show_fabric
        )

        self._current_view.pack()
