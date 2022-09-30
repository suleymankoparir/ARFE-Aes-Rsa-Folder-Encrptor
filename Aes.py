from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import os
class AesProtocol:
    @staticmethod
    def encryption (key, file_path,output_path,file_name):
        key = str.encode(key)
        cipher = AES.new(key, AES.MODE_CBC)
        file=open(os.path.join(file_path, file_name),'rb').read()
        cipher_text = cipher.encrypt(pad(file, AES.block_size))
        
        with open(os.path.join(output_path, file_name), 'wb') as kfile:
            kfile.write(cipher.iv)
            kfile.write(cipher_text)
    @staticmethod
    def decryption (key, file_path,output_path,file_name):
        key = str.encode(key)
        with open(os.path.join(file_path, file_name),'rb') as c_text:
            iv = c_text.read(16)
            ct = c_text.read()
        cipher = AES.new(key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        file=open(os.path.join(output_path, file_name),'wb')
        file.write(pt)
        file.close()