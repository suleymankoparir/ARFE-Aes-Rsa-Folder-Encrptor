from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from Aes import AesProtocol
from Rsa import RsaProtocol
from ttkthemes import ThemedTk
import os

class App:
    def __init__(self, root):
        root.title("ARFE | Aes&Rsa Folder Encryptor")
        self.root=root
        width=550
        height=300
        self.filepath=''
        self.keypath=''
        self.privatekey=''
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        s = ttk.Style()
        s.configure('.', font=('Helvetica', 9))
        
        folderbutton=ttk.Button(root)
        folderbutton["text"] = "Select Folder"
        folderbutton.place(x=10,y=10,width=150,height=50)
        folderbutton["command"] = self.select_folder

        self.folderlabel=ttk.Label(root,font=('Helvetica', 9))
        self.folderlabel["text"] = ""
        self.folderlabel.place(x=180,y=10,width=360,height=50)

        keybutton=ttk.Button(root)
        keybutton["text"] = "Select Key"
        keybutton.place(x=10,y=70,width=150,height=50)
        keybutton["command"] = self.select_key

        self.keylabel=ttk.Label(root,font=('Helvetica', 9))
        self.keylabel["text"] = ""
        self.keylabel.place(x=180,y=70,width=360,height=50)
        
        privatekeybutton=ttk.Button(root)
        privatekeybutton["text"] = "Select Private Key"
        privatekeybutton.place(x=10,y=130,width=150,height=50)
        privatekeybutton["command"] = self.private_key

        self.privatekeylabel=ttk.Label(root,font=('Helvetica', 9))
        self.privatekeylabel["text"] = ""
        self.privatekeylabel.place(x=180,y=130,width=360,height=50)
        
        self.progresbar = ttk.Progressbar(root, length=100, mode='determinate')
        self.progresbar.place(x=10,y=190,width=530,height=20)

        encrptbutton=ttk.Button(root)
        encrptbutton["text"] = "Encrypt"
        encrptbutton.place(x=10,y=220,width=260,height=70)
        encrptbutton["command"] = self.encrypt

        decryptbutton=ttk.Button(root)
        decryptbutton["text"] = "Decrypt"
        decryptbutton.place(x=280,y=220,width=260,height=70)
        decryptbutton["command"] = self.decrypt
    def private_key(self):
        filetypes = (('pem files', '*.pem'),('all files', '*.*'))
        self.privatekey=filedialog.askopenfilename(filetypes=filetypes)
        self.privatekeylabel["text"]=self.privatekey
    def select_folder(self):
        self.filepath = filedialog.askdirectory()
        self.folderlabel["text"]=self.filepath
    def select_key(self):
        filetypes = (('bin files', '*.bin'),('all files', '*.*'))
        self.keypath = filedialog.askopenfilename(filetypes=filetypes)
        self.keylabel["text"]=self.keypath
    def encrypt(self):
        if not os.path.exists(self.filepath):
            messagebox.showerror("folderpath", "Select folder path")
        if not os.path.exists(self.keypath):
            messagebox.showerror("keyfile", "Select key file")
        if not os.path.exists(self.privatekey):
            messagebox.showerror("privatekeyfile", "Select private key file")
        password=RsaProtocol.decryption(self.privatekey,self.keypath)
        items=os.listdir(self.filepath)
        pbvalue=100/len(items)
        self.progresbar["value"]=0
        for item in items:
            self.progresbar["value"]+=pbvalue
            AesProtocol.encryption(password, self.filepath, self.filepath, item)
            self.root.update()
        self.progresbar["value"]=0
        messagebox.showinfo("Encryption","Encryption completed")
    def decrypt(self):
        if not os.path.exists(self.filepath):
            messagebox.showerror("folderpath", "Select folder path")
        if not os.path.exists(self.keypath):
            messagebox.showerror("keyfile", "Select key file")
        if not os.path.exists(self.privatekey):
            messagebox.showerror("privatekeyfile", "Select private key file")
        password=RsaProtocol.decryption(self.privatekey,self.keypath)
        items=os.listdir(self.filepath)
        self.progresbar["value"]=0
        pbvalue=100/len(items)
        for item in items:
            self.progresbar["value"]+=pbvalue
            AesProtocol.decryption(password, self.filepath, self.filepath, item)
            self.root.update()
        self.progresbar["value"]=0
        messagebox.showinfo("Decryption","Decryption completed")
if __name__ == "__main__":
    root = ThemedTk(theme='breeze')
    app = App(root)
    root.mainloop()

