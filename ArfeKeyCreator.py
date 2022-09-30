from Rsa import RsaProtocol
import os
import sys
def main():
    path=sys.argv[1]
    password=sys.argv[2]
    if not os.path.exists(path):
        print("path does not exist")
        sys.exit()
    if not len(password)==32:
        print("password does not contain 32 character")
        sys.exit()
    RsaProtocol.create_key(path)
    RsaProtocol.encryption(os.path.join(path, "public.pem"), path, password)
    print("Key generation completed")
    
    
if __name__ == "__main__":
    main()

