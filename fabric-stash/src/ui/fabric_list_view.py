import tkinter as tk
import tkinter.ttk as ttk
from tkinter import constants

from services.fabric_service import FabricService


class FabricListView:
    def __init__(self, root, handle_add, handle_search,
                 handle_show_fabric):
        self._root = root
        self._handle_add = handle_add
        self._handle_search = handle_search
        self._handle_show_fabric = handle_show_fabric
        self._frame = None

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

        fabric_list = self._fabric_frame(self._frame)
        fabric_list.grid(row=2, sticky=tk.EW)

        buttons = self._button_frame(self._frame)
        buttons.grid(row=10)

    def _fabric_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        fabric_ids = self._service.get_all_ids()

        if not fabric_ids:
            no_fabrics_button = ttk.Button(
                frame,
                text="no fabrics, add new",
                command=self._handle_add
            )
            no_fabrics_button.grid(row=0)
        else:
            for fabric_id in fabric_ids:
                fabric = self._service.get_fabric_by_id(fabric_id)
                fabric_button = ttk.Button(
                    frame,
                    text=str(fabric),
                    command=lambda i=fabric_id: self._handle_show_fabric(i)
                )
                fabric_button.grid(row=fabric_id)

        return frame

    def _button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        button_add = ttk.Button(
            frame,
            text="add fabric",
            command=self._handle_add
        )
        button_add.grid(row=0, column=0, padx=4)

        button_search = ttk.Button(
            frame,
            text="search",
            command=self._handle_search
        )
        button_search.grid(row=0, column=1, padx=4)

        return frame
