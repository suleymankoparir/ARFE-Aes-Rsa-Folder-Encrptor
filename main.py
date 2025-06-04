import tkinter as tk
from tkinter import ttk

from tabs.key_generator_tab import KeyGeneratorTab
from tabs.key_recreate_tab import KeyRecreateTab
from tabs.folder_encryptor_tab import FolderEncryptorTab
from tabs.file_encryptor_tab import FileEncryptorTab

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Encryptor Application")
        self.geometry("600x400")
        self.resizable(False, False)

        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)

        KeyGeneratorTab(notebook)
        KeyRecreateTab(notebook)
        FolderEncryptorTab(notebook)
        FileEncryptorTab(notebook)

if __name__ == "__main__":
    app = App()
    app.mainloop()