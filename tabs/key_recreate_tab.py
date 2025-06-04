import os
from tkinter import ttk, filedialog, messagebox, StringVar

from encryptions.rsa import RsaProtocol

class KeyRecreateTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.add(self, text='Key Recreate')
        self.configure(padding=20)

        style = ttk.Style()
        style.theme_use('default')
        style.configure('TLabel', font=('Segoe UI', 11), foreground='#333')
        style.configure('TEntry', font=('Segoe UI', 10))
        style.configure('TButton',
                        font=('Segoe UI Semibold', 11),
                        foreground='white',
                        background='#0052cc',
                        padding=8)
        style.map('TButton',
                  foreground=[('active', 'white')],
                  background=[('active', '#003d99')])

        # Output folder
        ttk.Label(self, text="Select output folder:").grid(row=0, column=0, sticky='w', pady=(0,5))
        self.output_folder_var = StringVar()
        self.output_folder_entry = ttk.Entry(self, textvariable=self.output_folder_var, width=45)
        self.output_folder_entry.grid(row=1, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.browse_output_folder).grid(row=1, column=1, sticky='ew', padx=(10,0))

        # Public key
        ttk.Label(self, text="Select existing public key (.pem):").grid(row=2, column=0, sticky='w', pady=(0,5))
        self.pub_key_var = StringVar()
        self.pub_key_entry = ttk.Entry(self, textvariable=self.pub_key_var, width=45)
        self.pub_key_entry.grid(row=3, column=0, sticky='ew', pady=(0,10))
        ttk.Button(self, text="Browse", command=self.browse_pub_key).grid(row=3, column=1, sticky='ew', padx=(10,0))

        # Password
        ttk.Label(self, text="Password (32 chars):").grid(row=4, column=0, sticky='w', pady=(0,5))
        self.password_var = StringVar()
        self.password_entry = ttk.Entry(self, textvariable=self.password_var, width=45, show='*')
        self.password_entry.grid(row=5, column=0, sticky='ew', pady=(0,15))

        # Recreate button
        ttk.Button(self, text="Recreate Keys", command=self.recreate_keys).grid(row=6, column=0, columnspan=2, sticky='ew')

        self.columnconfigure(0, weight=1)

    def browse_output_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder_var.set(folder)

    def browse_pub_key(self):
        file = filedialog.askopenfilename(filetypes=[("PEM files", "*.pem")])
        if file:
            self.pub_key_var.set(file)

    def recreate_keys(self):
        output_folder = self.output_folder_var.get()
        pub_key_path = self.pub_key_var.get()
        password = self.password_var.get()

        if not os.path.exists(output_folder):
            messagebox.showerror("Error", "Output folder path does not exist.")
            return
        if not os.path.exists(pub_key_path):
            messagebox.showerror("Error", "Public key file does not exist.")
            return
        if len(password) != 32:
            messagebox.showerror("Error", "Password must be exactly 32 characters long.")
            return

        try:
            RsaProtocol.encryption(pub_key_path, output_folder, password)
            messagebox.showinfo("Success", "Keys recreated successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Key recreation failed: {str(e)}")