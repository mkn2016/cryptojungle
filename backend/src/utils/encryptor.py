from re import sub
from base64 import b64encode
from Crypto.Util.Padding import pad
from Crypto.Cipher.AES import new, block_size, MODE_CFB


class Encrypt(object):
    def __init__(self, filename, password):
        self.filename = filename
        self.password = password.encode("utf-8")
        self.block_size = block_size
    
    def encode_with_b64(self, to_be_encoded):
        return b64encode(to_be_encoded).decode("utf-8")
    
    def to_be_padded(self, data):
        return pad(data, self.block_size)
    
    def generate_cipher_from_key(self, key):
        return new(key, MODE_CFB)
    
    def encrypt(self):
        key = self.to_be_padded(self.password)
        cipher = self.generate_cipher_from_key(key)

        with open(self.filename, 'rb') as file:
            data = file.read()
            data = self.to_be_padded(data)
            cipher_text = cipher.encrypt(data)
            iv = self.encode_with_b64(cipher.iv)
            cipher_text = self.encode_with_b64(cipher_text)
            write_to_file = iv + cipher_text
            with open(sub(".pdf", "", self.filename) + ".enc", "w") as data:
                data.write(write_to_file)


