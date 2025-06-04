import os
from tkinter import ttk, messagebox, StringVar, filedialog
from encryptions.rsa import RsaProtocol

class KeyGeneratorTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)
        parent.add(self, text='Key Generator')

        self.columnconfigure(0, weight=1)

        ttk.Label(self, text="Select folder to save keys:").grid(row=0, column=0, sticky='w', pady=(0, 5))
        self.keygen_path_var = StringVar()
        self.keygen_path_entry = ttk.Entry(self, textvariable=self.keygen_path_var)
        self.keygen_path_entry.grid(row=1, column=0, sticky='ew')
        ttk.Button(self, text="Browse", command=self.keygen_browse).grid(row=1, column=1, sticky='ew', padx=(10,0), pady=2)

        ttk.Label(self, text="Password (32 chars):").grid(row=2, column=0, sticky='w', pady=(15, 5))
        self.keygen_password_var = StringVar()
        self.keygen_password_entry = ttk.Entry(self, textvariable=self.keygen_password_var)
        self.keygen_password_entry.grid(row=3, column=0, columnspan=2, sticky='ew')

        ttk.Button(self, text="Generate Keys", command=self.generate_keys).grid(
            row=4, column=0, columnspan=2, sticky='ew', pady=(20, 0), ipadx=5, ipady=10)

    def keygen_browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.keygen_path_var.set(folder)

    def generate_keys(self):
        path = self.keygen_path_var.get()
        password = self.keygen_password_var.get()

        if not os.path.exists(path):
            messagebox.showerror("Error", "Selected folder path does not exist.")
            return
        if len(password) != 32:
            messagebox.showerror("Error", "Password must be exactly 32 characters long.")
            return
        try:
            RsaProtocol.create_key(path)
            pubkey_path = os.path.join(path, "public.pem")
            RsaProtocol.encryption(pubkey_path, path, password)
            messagebox.showinfo("Success", "Key generation completed.")
        except Exception as e:
            messagebox.showerror("Error", f"Key generation failed: {str(e)}")
