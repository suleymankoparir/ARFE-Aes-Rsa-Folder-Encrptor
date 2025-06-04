import os
from tkinter import ttk, filedialog, messagebox, StringVar
from encryptions.rsa import RsaProtocol
from encryptions.aes import AesProtocol

class FileEncryptorTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.add(self, text='File Encryptor')
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

        ttk.Label(self, text="Select file to encrypt/decrypt:").grid(row=0, column=0, sticky='w', pady=(0,5))
        self.file_var = StringVar()
        self.file_entry = ttk.Entry(self, textvariable=self.file_var, width=50)
        self.file_entry.grid(row=1, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.select_file).grid(row=1, column=1, sticky='ew', padx=(10,0))

        ttk.Label(self, text="Select key file (.bin):").grid(row=2, column=0, sticky='w', pady=(0,5))
        self.key_var = StringVar()
        self.key_entry = ttk.Entry(self, textvariable=self.key_var, width=50)
        self.key_entry.grid(row=3, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.select_key).grid(row=3, column=1, sticky='ew', padx=(10,0))

        ttk.Label(self, text="Select private key (.pem):").grid(row=4, column=0, sticky='w', pady=(0,5))
        self.private_key_var = StringVar()
        self.private_key_entry = ttk.Entry(self, textvariable=self.private_key_var, width=50)
        self.private_key_entry.grid(row=5, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.select_private_key).grid(row=5, column=1, sticky='ew', padx=(10,0))

        # Buttons
        ttk.Button(self, text="Encrypt", command=self.encrypt).grid(row=6, column=0, sticky='ew', padx=(0,5), pady=(10,0))
        ttk.Button(self, text="Decrypt", command=self.decrypt).grid(row=6, column=1, sticky='ew', padx=(5,0), pady=(10,0))

        self.columnconfigure(0, weight=1)

    def select_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.file_var.set(file)

    def select_key(self):
        file = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin")])
        if file:
            self.key_var.set(file)

    def select_private_key(self):
        file = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem")])
        if file:
            self.private_key_var.set(file)

    def encrypt(self):
        file = self.file_var.get()
        key_file = self.key_var.get()
        private_key_file = self.private_key_var.get()

        if not os.path.isfile(file):
            messagebox.showerror("Error", "Select a valid file.")
            return
        if not os.path.exists(key_file):
            messagebox.showerror("Error", "Select a valid key (.bin) file.")
            return
        if not os.path.exists(private_key_file):
            messagebox.showerror("Error", "Select a valid private key (.pem) file.")
            return

        password = RsaProtocol.decryption(private_key_file, key_file)
        try:
            AesProtocol.encryption(password, os.path.dirname(file), os.path.dirname(file), os.path.basename(file))
            messagebox.showinfo("Success", "File encrypted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt(self):
        file = self.file_var.get()
        key_file = self.key_var.get()
        private_key_file = self.private_key_var.get()

        if not os.path.isfile(file):
            messagebox.showerror("Error", "Select a valid file.")
            return
        if not os.path.exists(key_file):
            messagebox.showerror("Error", "Select a valid key (.bin) file.")
            return
        if not os.path.exists(private_key_file):
            messagebox.showerror("Error", "Select a valid private key (.pem) file.")
            return

        password = RsaProtocol.decryption(private_key_file, key_file)
        try:
            AesProtocol.decryption(password, os.path.dirname(file), os.path.dirname(file), os.path.basename(file))
            messagebox.showinfo("Success", "File decrypted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")