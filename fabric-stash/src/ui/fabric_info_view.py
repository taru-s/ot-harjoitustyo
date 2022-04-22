import tkinter as tk
import tkinter.ttk as ttk
from entities.fabric import Fabric

class FabricInfoView():
    def __init__(self, root, fabric:Fabric,handle_edit, handle_delete, handle_back):
        self._root = root
        self._fabric = fabric
        self._handle_edit = handle_edit
        self._handle_delete = handle_delete
        self._handle_back = handle_back
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0, padx=2, pady=2)

    def destroy(self):
        for w in self._frame.winfo_children():
            w.destroy()
        self._fabric = None
        self._frame.destroy()


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        # label_header = ttk.Label(master=self._root, text=self._fabric.name, anchor=tk.N)
        # label_header.grid(row=0)

        fabric_info = self._initialize_fabric_info_frame(self._frame)
        fabric_info.grid(row=2, sticky=tk.EW)

        buttons = self._initialize_button_frame(self._frame)
        buttons.grid(row=10)

    def _initialize_fabric_info_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        property_names = list(Fabric.fabric_properties_and_types().keys())
        fabric_values = self._fabric.get_values()
        properties = []

        for i in range(len(property_names)):
            properties.append(f"{property_names[i]}: {fabric_values[i]}")

        property_fields = []
                
        for prop in properties:
            label = ttk.Label(frame, text=prop)
            property_fields.append(label)

        for i in range(len(property_fields)):
            property_fields[i].grid(row=i)

        return frame

    def _initialize_button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        button_edit = ttk.Button(
            frame,
            text="edit",
            command=lambda: self._handle_edit(self._fabric)
        )
        button_edit.grid(row=0, column=0, padx=4)

        button_delete = ttk.Button(
            frame,
            text="delete",
            command=self._handle_delete
        )
        button_delete.grid(row=0, column=1, padx=4)

        button_list = ttk.Button(
            frame,
            text="list",
            command=self._handle_back
        )
        button_list.grid(row=0, column=3, padx=4)
        
        return frame