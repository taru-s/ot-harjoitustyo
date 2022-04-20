from asyncio import constants
import tkinter

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import constants

class FabricListView:
    def __init__(self, root, handle_add, handle_search):
        self._root = root
        self._handle_add = handle_add
        self._handle_search = handle_search
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        label_header = ttk.Label(master=self._frame, text="Fabric list", anchor=tk.N)
        label_header.grid(row=0)

        button_add = ttk.Button(
            master=self._frame, 
            text="add fabric",
            command=self._handle_add
        )
        button_add.grid(row=100, column=0)

        button_search = ttk.Button(
            master=self._frame,
            text="search",
            command=self._handle_search
        )
        button_search.grid(row=100, column=1)


    