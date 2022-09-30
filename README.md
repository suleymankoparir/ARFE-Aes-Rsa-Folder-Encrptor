# ARFE-Aes&Rsa Folder Encrptor
 This software encrypts and decrypts files using aes key encrypted with rsa.

### Key Generation
Keys can be generated in two different ways.
- Rsa keys and aes key are generated at the same time.
```
python ArfeKeyCreator.py [path] [password]
```
Key must contain 32 characters

**Example usage**
```
python ArfeKeyCreator.py C:\Users\johndoe\Desktop\keys 3ShIofRMm4zyLws1xc7RWxNyD2Le2MKc
```

- Generate an aes key with an existing public key.
```
python ArfeKeyCreatorFromPublic.py [path] [keypath] [password]
```
**Example usage**
```
python ArfeKeyCreatorFromPublic.py C:\Users\johndoe\Desktop\keys C:\Users\johndoe\Desktop\keys\public.pem 3ShIofRMm4zyLws1xc7RWxNyD2Le2MKc
```
### UI
[![](https://i.imgur.com/iuVmDSV.jpeg)](https://i.imgur.com/iuVmDSV.jpeg)


### Libraries
- tkinter
- ttkthemes
- pycryptodome
