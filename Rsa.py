from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import os
class RsaProtocol:
    @staticmethod
    def create_key(key_path):
        key = RSA.generate(2048)
        private_key = key.exportKey()
        with open(os.path.join(key_path, 'private.pem'),"wb") as f:
            f.write(private_key)
        public_key = key.publickey().exportKey()
        with open(os.path.join(key_path, 'public.pem'), "wb") as f:
            f.write(public_key)
    @staticmethod
    def encryption(key_path,output_path,data_text):
        data = data_text.encode("utf-8")
        with open(os.path.join(output_path, "crypted_key.bin"), "wb") as f:
            recipient_key = RSA.import_key(open(key_path).read())
            session_key = get_random_bytes(16)
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            [ f.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    @staticmethod
    def decryption(key_path, data_path):
        with open(data_path, "rb") as f:
            private_key = RSA.import_key(open(key_path).read())
            enc_session_key, nonce, tag, ciphertext = \
               [ f.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            return data.decode("utf-8")
    