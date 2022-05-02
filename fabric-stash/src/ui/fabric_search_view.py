import tkinter as tk
import tkinter.ttk as ttk

from services.fabric_service import FabricService


class FabricSearchView:
    def __init__(self, root, handle_add, handle_list, handle_show_fabric):
        self._root = root
        self._handle_add = handle_add
        self._handle_list = handle_list
        self._handle_show_fabric = handle_show_fabric
        self._frame = None

        self._search_var = tk.StringVar()
        self._fabric_list_frame = None

        self._service = FabricService()

        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0, padx=2, pady=2)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        label_header = ttk.Label(
            master=self._frame, text="Fabric list", anchor=tk.N)
        label_header.grid(row=0)

        search_bar = self._search_frame(self._frame)
        search_bar.grid(row=1)

        self._fabric_list_frame = self._fabric_frame(self._frame)
        self._fabric_list_frame.grid(row=2, sticky=tk.EW)

        buttons = self._button_frame(self._frame)
        buttons.grid(row=10)

    def _search_frame(self, container):
        frame = ttk.Frame(container, padding=3)
        search_text_entry = ttk.Entry(frame, textvariable=self._search_var) 
        search_text_entry.grid(column=0, columnspan=2)

        search_button = ttk.Button(frame, text="search", command= self._update_fabric_list)
        search_button.grid(column=3)
        return frame

    def _fabric_frame(self, container):
        frame = ttk.Frame(container, padding=3)
        return frame

    def _button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        button_add = ttk.Button(
            frame,
            text="add fabric",
            command=self._handle_add
        )
        button_add.grid(row=0, column=0, padx=4)

        button_list = ttk.Button(
            frame,
            text="list",
            command=self._handle_list
        )
        button_list.grid(row=0, column=3, padx=4)

        return frame

    def _update_fabric_list(self):
        for widget in self._fabric_list_frame.winfo_children():
            widget.destroy()
        search_term = self._search_var.get()
        fabric_ids = self._service.get_fabrics_by_name(search_term)

        if not fabric_ids:
            no_fabrics_label = ttk.Label(
                self._fabric_list_frame,
                text="no fabrics found"
            )

            no_fabrics_label.grid(row=0)
        else:
            for fabric_id in fabric_ids:
                fabric = self._service.get_fabric_by_id(fabric_id)
                fabric_button = ttk.Button(
                    self._fabric_list_frame,
                    text=str(fabric),
                    command=lambda i = fabric_id: self._handle_show_fabric(i)
                )
                fabric_button.grid(row=fabric_id)