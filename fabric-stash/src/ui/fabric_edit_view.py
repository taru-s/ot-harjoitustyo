import tkinter as tk
import tkinter.ttk as ttk
from entities.fabric import Fabric

class FabricEditView():
    def __init__(self, root, fabric: Fabric, handle_save, handle_delete, handle_cancel):
        self._root = root
        self._fabric = fabric
        self._handle_save = handle_save
        self._handle_delete = handle_delete
        self._handle_cancel = handle_cancel
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.grid(row=0, column=0, padx=2, pady=2)

    def destroy(self):
        for widget in self._frame.winfo_children():
            widget.destroy()
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        fabric_info = self._fabric_info_edit_frame(self._root)
        fabric_info.grid(row=2, sticky=tk.EW)

        buttons = self._button_frame(self._root)
        buttons.grid(row=10)

    def _fabric_info_edit_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        properties_and_types = Fabric.fabric_properties_and_types()
        fabric_values = self._fabric.get_values()

        properties_types_list = list(properties_and_types.items())

        for i in range(len(properties_types_list)):
            # create frame containing the property name followed by 
            # appropriate input method widget, add to list of all 
            # property-input-frames, in a separate loop add all these
            # frames to the whole info frame to be returned 
            # TODO extract to own method?

            prop_label_text = properties_types_list[i][0]
            prop_label = ttk.Label(frame, text=prop_label_text)

            if properties_types_list[i][1] == str:
                input_text = tk.StringVar()
                input_widget = ttk.Entry(frame, textvariable=input_text)
            elif properties_types_list[i][1] == int:
                input_text = tk.IntVar()
                input_widget = ttk.Entry(frame, textvariable=input_text)
            elif properties_types_list[i][1] == bool:
                input_widget = ttk.Checkbutton(frame, onvalue=1, offvalue=0)
            
            prop_label.grid(row=i, column=0)
            input_widget.grid(row=i, column=1)

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
            command=self._handle_delete
        )
        button_delete.grid(row=0, column=1, padx=4)

        button_cancel = ttk.Button(
            frame,
            text="cancel",
            command=lambda: self._handle_cancel(self._fabric)
        )
        button_cancel.grid(row=0, column=3, padx=4)
        
        return frame