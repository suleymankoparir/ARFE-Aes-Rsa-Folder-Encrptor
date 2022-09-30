from Rsa import RsaProtocol
import os
import sys
def main():
    path=sys.argv[1]
    keypath=sys.argv[2]
    password=sys.argv[3]
    if not os.path.exists(path):
        print("path does not exist")
        sys.exit()
    if not os.path.exists(keypath):
        print("keypath does not exist")
        sys.exit()
    if not len(password)==32:
        print("password does not contain 32 character")
        sys.exit()
    RsaProtocol.encryption(keypath, path, password)
    print("Key generation completed")
    
    
if __name__ == "__main__":
    main()
