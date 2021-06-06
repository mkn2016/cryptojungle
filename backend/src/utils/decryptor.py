from re import sub
from base64 import b64decode
from Crypto.Util.Padding import unpad, pad
from Crypto.Cipher.AES import new, block_size, MODE_CFB


class Decrypt(object):
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password.encode("utf-8")
        self.block_size = block_size
    
    def to_be_padded(self, data):
        return pad(data, self.block_size)
    
    def to_be_unpadded(self, data):
        return unpad(data, self.block_size)
    
    def generate_cipher_with_key_and_iv(self, key, iv):
        return new(key, MODE_CFB, iv)
    
    def decrypt(self):
        key = self.to_be_padded(self.password)

        with open(self.filename, "r") as file:
            data = file.read()
            length = len(data)
            iv = data[:24]
            iv = b64decode(iv)
            cipher_text = data[24:length]
            cipher_text = b64decode(cipher_text)
            cipher = self.generate_cipher_with_key_and_iv(key, iv)
            decrypted = cipher.decrypt(cipher_text)
            decrypted = self.to_be_unpadded(decrypted)
            with open(sub(".enc", "", self.filename) + ".pdf", "wb") as data:
                data.write(decrypted)
