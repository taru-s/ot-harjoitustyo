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

        self._name_var = tk.StringVar()
        self._width_var = tk.IntVar()
        self._length_var = tk.IntVar()
        self._washed_var = tk.BooleanVar()

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

        fabric = self._service.get_fabric_by_id(self._fabric_id)

        header_current_label = ttk.Label(frame, text="current")
        header_new_label = ttk.Label(frame, text="new")
        header_current_label.grid(row=0, column=1)
        header_new_label.grid(row=0,column=2)

        name_label = ttk.Label(frame, text="name")
        current_name_label = ttk.Label(frame, text=fabric.name)        
        name_entry = ttk.Entry(frame, textvariable=self._name_var)

        name_label.grid(row=10,column=0)
        current_name_label.grid(row=10,column=1)
        name_entry.grid(row=10,column=2)

        width_label = ttk.Label(frame, text="width")
        width_current_label = ttk.Label(frame, text=fabric.width)
        width_entry = ttk.Entry(frame, textvariable=self._width_var)

        width_label.grid(row=20,column=0)
        width_current_label.grid(row=20,column=1)
        width_entry.grid(row=20,column=2)

        length_label = ttk.Label(frame, text="length")
        length_current_label = ttk.Label(frame, text=fabric.length)
        length_entry = ttk.Entry(frame, textvariable=self._length_var)

        length_label.grid(row=30,column=0)
        length_current_label.grid(row=30,column=1)
        length_entry.grid(row=30,column=2)

        washed_label = ttk.Label(frame, text="washed")
        washed_current_label = ttk.Label(frame, text=self._washed_label_to_str(fabric.washed))
        washed_entry = ttk.Checkbutton(frame, variable=self._washed_var)

        washed_label.grid(row=40,column=0)
        washed_current_label.grid(row=40,column=1)
        washed_entry.grid(row=40,column=2)

        return frame

    def _button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        #TODO validate user input (width&length int)
        button_save = ttk.Button(
            frame,
            text="save",
            command=
                lambda 
                i = self._fabric_id,
                : self._handle_save(i, self._name_var.get(), 
                                        self._width_var.get(),
                                        self._length_var.get(),
                                        self._washed_var.get())
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

    def _washed_label_to_str(self, int_value):
        if int_value == 1:
            return "yes"
        elif int_value == 0:
            return "no"
        else:
            return "n/a"