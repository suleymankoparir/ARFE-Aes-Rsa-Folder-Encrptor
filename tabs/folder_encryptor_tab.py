import os
from tkinter import ttk, filedialog, messagebox, StringVar
from Rsa import RsaProtocol
from Aes import AesProtocol

class FolderEncryptorTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.add(self, text='Folder Encryptor')
        self.configure(padding=20)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TLabel', font=('Segoe UI', 11), foreground='#333')
        style.configure('TEntry', font=('Segoe UI', 10))
        style.configure('TButton',
                        font=('Segoe UI Semibold', 11),
                        foreground='white',
                        background='#007acc',
                        padding=8)
        style.map('TButton',
                  foreground=[('active', 'white')],
                  background=[('active', '#005ea3')])

        # Folder selection
        ttk.Label(self, text="Select folder to encrypt/decrypt:").grid(row=0, column=0, sticky='w', pady=(0,5))
        self.folder_var = StringVar()
        self.folder_entry = ttk.Entry(self, textvariable=self.folder_var, width=45)
        self.folder_entry.grid(row=1, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.select_folder).grid(row=1, column=1, sticky='ew', padx=(10,0))

        # Key file selection (.bin)
        ttk.Label(self, text="Select key file (.bin):").grid(row=2, column=0, sticky='w', pady=(0,5))
        self.key_var = StringVar()
        self.key_entry = ttk.Entry(self, textvariable=self.key_var, width=45)
        self.key_entry.grid(row=3, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.select_key).grid(row=3, column=1, sticky='ew', padx=(10,0))

        # Private key selection (.pem)
        ttk.Label(self, text="Select private key (.pem):").grid(row=4, column=0, sticky='w', pady=(0,5))
        self.private_key_var = StringVar()
        self.private_key_entry = ttk.Entry(self, textvariable=self.private_key_var, width=45)
        self.private_key_entry.grid(row=5, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.select_private_key).grid(row=5, column=1, sticky='ew', padx=(10,0))

        # Progressbar
        self.progressbar = ttk.Progressbar(self, mode='determinate')
        self.progressbar.grid(row=6, column=0, columnspan=2, sticky='ew', pady=(10,20))

        # Encrypt and Decrypt buttons
        ttk.Button(self, text="Encrypt", command=self.encrypt).grid(row=7, column=0, sticky='ew', padx=(0,5))
        ttk.Button(self, text="Decrypt", command=self.decrypt).grid(row=7, column=1, sticky='ew', padx=(5,0))

        self.columnconfigure(0, weight=1)

    def select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_var.set(folder)

    def select_key(self):
        file = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
        if file:
            self.key_var.set(file)

    def select_private_key(self):
        file = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem")])
        if file:
            self.private_key_var.set(file)

    def encrypt(self):
        folder = self.folder_var.get()
        key_file = self.key_var.get()
        private_key_file = self.private_key_var.get()

        if not os.path.exists(folder):
            messagebox.showerror("Error", "Select a valid folder path.")
            return
        if not os.path.exists(key_file):
            messagebox.showerror("Error", "Select a valid key (.bin) file.")
            return
        if not os.path.exists(private_key_file):
            messagebox.showerror("Error", "Select a valid private key (.pem) file.")
            return

        password = RsaProtocol.decryption(private_key_file, key_file)
        items = os.listdir(folder)
        if not items:
            messagebox.showinfo("Info", "Selected folder is empty.")
            return
        pb_value = 100 / len(items)
        self.progressbar["value"] = 0
        for item in items:
            self.progressbar["value"] += pb_value
            AesProtocol.encryption(password, folder, folder, item)
            self.update()
        self.progressbar["value"] = 0
        messagebox.showinfo("Success", "Encryption completed.")

    def decrypt(self):
        folder = self.folder_var.get()
        key_file = self.key_var.get()
        private_key_file = self.private_key_var.get()

        if not os.path.exists(folder):
            messagebox.showerror("Error", "Select a valid folder path.")
            return
        if not os.path.exists(key_file):
            messagebox.showerror("Error", "Select a valid key (.bin) file.")
            return
        if not os.path.exists(private_key_file):
            messagebox.showerror("Error", "Select a valid private key (.pem) file.")
            return

        password = RsaProtocol.decryption(private_key_file, key_file)
        items = os.listdir(folder)
        if not items:
            messagebox.showinfo("Info", "Selected folder is empty.")
            return
        pb_value = 100 / len(items)
        self.progressbar["value"] = 0
        for item in items:
            self.progressbar["value"] += pb_value
            AesProtocol.decryption(password, folder, folder, item)
            self.update()
        self.progressbar["value"] = 0
        messagebox.showinfo("Success", "Decryption completed.")