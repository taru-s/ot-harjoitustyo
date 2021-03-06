import tkinter as tk
import tkinter.ttk as ttk
from entities.fabric import Fabric
from services.fabric_service import FabricService


class FabricInfoView():
    def __init__(self, root, fabric_id, from_search, handle_edit, handle_delete, handle_back):
        self._service = FabricService()
        self._root = root
        self._fabric_id = fabric_id
        self._fabric = self._service.get_fabric_by_id(fabric_id)
        self._handle_edit = handle_edit
        self._handle_delete = handle_delete
        self._handle_back = handle_back
        self._frame = None

        self._from_search = from_search

        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0, padx=2, pady=2)

    def destroy(self):
        # for w in self._frame.winfo_children():
        #     w.destroy()
        self._fabric = None
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        fabric_info = self._initialize_fabric_info_frame(self._frame)
        fabric_info.grid(row=2, sticky=tk.W)

        buttons = self._initialize_button_frame(self._frame)
        buttons.grid(row=10)

    def _initialize_fabric_info_frame(self, container):
        """Creates the frame containing the fabric information.

        Args:
            container (Frame): The frame to which the info frame will be added.

        Returns:
            Frame: Frame containing the fabric information labels.
        """
        frame = ttk.Frame(container, padding=3)

        property_names = list(Fabric.properties_and_types().keys())
        fabric_values = self._fabric.get_values()
        properties = []

        for i, name in enumerate(property_names):
            if name == "washed":
                properties.append(f"{name}: {self._fabric.washed_to_str()}")
            else:
                properties.append(f"{name}: {fabric_values[i]}")

        property_fields = []

        for prop in properties:
            label = ttk.Label(frame, text=prop)
            property_fields.append(label)

        for i, name in enumerate(property_fields):
            name.grid(row=i)

        return frame

    def _initialize_button_frame(self, container):
        """Constructs the menu buttons on the bottom of the view.

        Args:
            container (Frame): The frame to which the list frame will be added.

        Returns:
            frame: The frame containing the buttons.
        """
        frame = ttk.Frame(container, padding=3)

        button_edit = ttk.Button(
            frame,
            text="edit",
            command=lambda: self._handle_edit(self._fabric_id)
        )
        button_edit.grid(row=0, column=0, padx=4)

        button_delete = ttk.Button(
            frame,
            text="delete",
            command=lambda i=self._fabric_id: self._handle_delete(i)
        )
        button_delete.grid(row=0, column=1, padx=4)

        button_back = ttk.Button(
            frame,
            text="back",
            command=lambda: self._handle_back(self._from_search)
        )
        button_back.grid(row=0, column=3, padx=4)

        return frame
