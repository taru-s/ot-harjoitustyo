import tkinter as tk
import tkinter.ttk as ttk
from services.fabric_service import FabricService
from entities.fabric import Fabric


class FabricEditView():
    def __init__(self, root, fabric_id, from_add_new, handle_save, handle_delete, handle_cancel):
        self._service = FabricService()

        self._root = root
        self._fabric_id = fabric_id
        self._fabric = self._service.get_fabric_by_id(self._fabric_id)
        self._handle_save = handle_save
        self._handle_delete = handle_delete
        self._handle_cancel = handle_cancel
        self._frame = None

        self._from_add_new = from_add_new

        self._name_var = tk.StringVar(value=self._fabric.name)
        self._width_var = tk.IntVar(value=self._fabric.width)
        self._length_var = tk.IntVar(value=self._fabric.length)
        self._washed_var = tk.IntVar(value=self._fabric.washed)
        self._error_var = tk.StringVar(value="")

        # TODO save button enabling/disabling?
        self._save_enabled_var = tk.StringVar(value="enabled")

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

        error_message = self._error_message(self._frame)
        error_message.grid(row=9)

        buttons = self._button_frame(self._frame)
        buttons.grid(row=10)

    def _fabric_info_edit_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        header_current_label = ttk.Label(frame, text="current")
        header_new_label = ttk.Label(frame, text="new")
        header_current_label.grid(row=0, column=1)
        header_new_label.grid(row=0, column=2)

        name_label = ttk.Label(frame, text="name")
        current_name_label = ttk.Label(frame, text=self._fabric.name)
        name_entry = ttk.Entry(frame, textvariable=self._name_var)

        name_label.grid(row=10, column=0)
        current_name_label.grid(row=10, column=1)
        name_entry.grid(row=10, column=2)

        width_label = ttk.Label(frame, text="width")
        width_current_label = ttk.Label(frame, text=self._fabric.width)
        width_entry = ttk.Entry(frame, textvariable=self._width_var)

        width_label.grid(row=20, column=0)
        width_current_label.grid(row=20, column=1)
        width_entry.grid(row=20, column=2)

        length_label = ttk.Label(frame, text="length")
        length_current_label = ttk.Label(frame, text=self._fabric.length)
        length_entry = ttk.Entry(frame, textvariable=self._length_var)

        length_label.grid(row=30, column=0)
        length_current_label.grid(row=30, column=1)
        length_entry.grid(row=30, column=2)

        washed_label = ttk.Label(frame, text="washed")
        washed_current_label = ttk.Label(
            frame, text=self._fabric.washed_to_str())
        washed_entry = ttk.Checkbutton(
            frame, variable=self._washed_var, onvalue=1, offvalue=0)

        washed_label.grid(row=40, column=0)
        washed_current_label.grid(row=40, column=1)
        washed_entry.grid(row=40, column=2)

        self._width_var.trace("w", self._validate_width_and_length)
        self._length_var.trace("w", self._validate_width_and_length)

        return frame

    def _error_message(self, container):
        frame = ttk.Frame(container)
        error_label = ttk.Label(frame, textvariable=self._error_var, foreground="red")
        error_label.grid()
        return frame

    def _set_error_message(self, boolean):
        if boolean:
            self._error_var.set(
                "width and length have to be postive integers")
        else:
            self._error_var.set("")

    def _validate_width_and_length(self, *args):
        try:
            self._width_var.get()
            self._length_var.get()
            self._set_error_message(False)
        except:
            self._set_error_message(True)

    def _press_save_button(self):
        if self._error_var.get() == "":
            self._handle_save(self._fabric_id,
                              self._name_var.get(),
                              self._width_var.get(),
                              self._length_var.get(),
                              self._washed_var.get())

    def _button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        button_save = ttk.Button(
            frame,
            text="save",
            command=lambda: self._press_save_button(),
            state=self._save_enabled_var.get
        )
        button_save.grid(row=0, column=0, padx=4)

        button_delete = ttk.Button(
            frame,
            text="delete",
            command=lambda i=self._fabric_id: self._handle_delete(i)
        )
        button_delete.grid(row=0, column=1, padx=4)

        button_cancel = ttk.Button(
            frame,
            text="cancel",
            command=lambda: self._handle_cancel(
                self._from_add_new, self._fabric_id)
        )
        button_cancel.grid(row=0, column=3, padx=4)

        return frame
