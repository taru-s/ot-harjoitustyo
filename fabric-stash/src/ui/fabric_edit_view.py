import tkinter as tk
import tkinter.ttk as ttk
from entities.fabric import Fabric
from services.fabric_service import FabricService

class FabricEditView():
    def __init__(self, root, fabric_id, handle_save, handle_delete, handle_cancel):
        self._root = root
        self._fabric_id = fabric_id
        self._handle_save = handle_save
        self._handle_delete = handle_delete
        self._handle_cancel = handle_cancel
        self._frame = None

        self._service = FabricService()

        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0, padx=2, pady=2)

    def destroy(self):
        for widget in self._frame.winfo_children():
            widget.destroy()
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        fabric_info = self._fabric_info_edit_frame(self._frame)
        fabric_info.grid(row=2, sticky=tk.EW)

        buttons = self._button_frame(self._frame)
        buttons.grid(row=10)

    def _fabric_info_edit_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        properties_and_types = Fabric.properties_and_types()
        fabric = self._service.get_fabric_by_id(self._fabric_id)
        fabric_values = fabric.get_values()

        properties_types_list = list(properties_and_types.items())

        header_current_label = ttk.Label(frame, text="current")
        header_new_label = ttk.Label(frame, text="new")
        header_current_label.grid(row=0, column=1)
        header_new_label.grid(row=0,column=2)

        name_label = ttk.Label(frame, text="name")
        current_name_label = ttk.Label(frame, text=fabric.name)
        name_input = tk.StringVar(frame, value=fabric.name)
        name_entry = ttk.Entry(frame, textvariable=name_input)

        name_label.grid(row=10,column=0)
        current_name_label.grid(row=10,column=1)
        name_entry.grid(row=10,column=2)

        width_label = ttk.Label(frame, text="width")
        width_current_label = ttk.Label(frame, text=fabric.width)
        width_input = tk.IntVar(frame, value=fabric.width)
        width_entry = ttk.Entry(frame, textvariable=width_input)

        width_label.grid(row=20,column=0)
        width_current_label.grid(row=20,column=1)
        width_entry.grid(row=20,column=2)

        length_label = ttk.Label(frame, text="length")
        length_current_label = ttk.Label(frame, text=fabric.length)
        length_input = tk.IntVar(frame, value=fabric.length)
        length_entry = ttk.Entry(frame, textvariable=length_input)

        length_label.grid(row=30,column=0)
        length_current_label.grid(row=30,column=1)
        length_entry.grid(row=30,column=2)


        return frame

    def _button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        button_save = ttk.Button(
            frame,
            text="save",
            command=self._handle_save
        )
        button_save.grid(row=0, column=0, padx=4)

        button_delete = ttk.Button(
            frame,
            text="delete",
            command=lambda i = self._fabric_id: self._handle_delete(i)
        )
        button_delete.grid(row=0, column=1, padx=4)

        button_cancel = ttk.Button(
            frame,
            text="cancel",
            command=lambda: self._handle_cancel(self._fabric_id)
        )
        button_cancel.grid(row=0, column=3, padx=4)

        return frame
