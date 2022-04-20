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
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        label_header = ttk.Label(master=self._frame, text=self._fabric.name, anchor=tk.N)
        label_header.grid(row=0)

        # fabric_list = self._fabric_frame(self._root)
        # fabric_list.grid(row=2, sticky=tk.EW)

        buttons = self._button_frame(self._root)
        buttons.grid(row=10)

    # def _fabric_frame(self, container): 
    #     frame = ttk.Frame(container, padding=3)

    #     fabrics = self._service.get_all_fabrics()
    #     fabric_buttons = []

    #     if not fabrics:
    #         no_fabrics_button = ttk.Button(
    #             frame,
    #             text="no fabrics, add new",
    #             command=self._handle_add
    #         )

    #         fabric_buttons.append(no_fabrics_button)
    #     else:
    #         for fabric in fabrics:
    #             fabric_button = ttk.Button(
    #                 frame,
    #                 text=str(fabric),
    #                 command=self._handle_show_fabric
    #             )

    #             fabric_buttons.append(fabric_button)

    #     for i in range(len(fabric_buttons)):
    #         fabric_buttons[i].grid(row=i)

    #     return frame

    def _button_frame(self, container):
        frame = ttk.Frame(container, padding=3)

        button_edit = ttk.Button(
            frame,
            text="edit",
            command=self._handle_edit
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
            text="back",
            command=self._handle_back
        )
        button_list.grid(row=0, column=3, padx=4)
        
        return frame